"""Remove hidden EXIF metadata (GPS location, camera, date) from a photo before you upload it.

    python strip_photo_metadata.py photo.jpg             # writes photo_clean.jpg
"""
import sys
from pathlib import Path

from PIL import Image
from PIL.ExifTags import IFD

GPS = IFD.GPSInfo


def describe(path):
    """Returns a short summary of the metadata a photo carries."""
    exif = Image.open(path).getexif()
    gps = exif.get_ifd(GPS)
    return {"tags": len(exif), "has_gps": bool(gps), "camera": exif.get(0x0110)}  # 0x0110 = camera model


def strip(path):
    """Saves a copy with only the pixels, and returns its path."""
    src = Path(path)
    out = src.with_name(f"{src.stem}_clean{src.suffix}")
    with Image.open(src) as img:
        clean = Image.new(img.mode, img.size)
        clean.paste(img)                     # copy pixels only: no EXIF, GPS or comments
        clean.save(out)
    return out


if __name__ == "__main__":
    photo = sys.argv[1]
    print("before:", describe(photo))
    cleaned = strip(photo)
    print("after: ", describe(cleaned), "->", cleaned)
