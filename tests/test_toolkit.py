import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from redact import redact  # noqa: E402
from strip_photo_metadata import describe, strip  # noqa: E402


def test_personal_data_is_masked():
    out = redact((ROOT / "examples" / "before.txt").read_text(encoding="utf-8"))
    for secret in ["98765 43210", "ravi.kumar@example.com", "4111 1111 1111 1111", "ABCDE1234F",
                   "2345 6789 0123", "10.20.30.40", "sk-proj-AbCdEfGhIjKlMnOpQrStUvWx", "Sup3rS3cret!"]:
        assert secret not in out
    for label in ["[PHONE]", "[EMAIL]", "[CARD]", "[PAN]", "[AADHAAR]", "[IP]", "[API_KEY]", "[SECRET]"]:
        assert label in out


def test_names_are_not_caught_so_always_read_the_result():
    assert "Ravi Kumar" in redact("My name is Ravi Kumar.")


def test_ordinary_text_is_unchanged():
    text = "Explain how a hash map works, with a Python example."
    assert redact(text) == text


def test_photo_metadata_is_removed(tmp_path):
    photo = tmp_path / "holiday.jpg"
    exif = Image.Exif()
    exif[0x0110] = "Pixel 9"
    exif.get_ifd(0x8825).update({1: "N", 2: (13.0, 4.0, 50.0), 3: "E", 4: (80.0, 16.0, 12.0)})
    Image.new("RGB", (32, 24), (200, 120, 80)).save(photo, exif=exif)
    assert describe(photo)["has_gps"]
    clean = strip(photo)
    assert describe(clean) == {"tags": 0, "has_gps": False, "camera": None}
    assert Image.open(clean).size == (32, 24)
