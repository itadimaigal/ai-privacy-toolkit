# AI Privacy Toolkit 🔒

Free tools and a checklist from the itadimaigal video
**"How to Stop AI From Using Your Data: ChatGPT & Claude Privacy Settings + 12 Real Examples"**.

Use AI tools without giving away your personal data, your company's data, or your secrets.

## Tools

| File | What it does |
|---|---|
| `redact.py` | Masks phone numbers, emails, Aadhaar, PAN, card numbers, API keys, passwords and IP addresses **before** you paste text into an AI chat |
| `strip_photo_metadata.py` | Removes hidden EXIF data (GPS location, phone model, date) from a photo before you upload it |
| `robots.txt` | Asks AI companies' training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot) not to collect your website |

### Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Redact text before you paste it

```bash
python redact.py examples/before.txt
```

```
My name is Ravi Kumar, phone [PHONE], email [EMAIL].
My card [CARD] was charged twice. My PAN is [PAN]
and my Aadhaar is [AADHAAR]. Our office server is [IP].
    OPENAI_API_KEY = "[API_KEY]"
    db_password: [SECRET]
```

⚠️ Notice that the **name** is still there. Patterns can't catch names, addresses or context.
**Always read the result before you paste it.** All the example data is fake.

### Remove hidden data from a photo

```bash
python strip_photo_metadata.py examples/holiday.jpg
```

```
before: {'tags': 3, 'has_gps': True, 'camera': 'Pixel 9'}
after:  {'tags': 0, 'has_gps': False, 'camera': None} -> examples/holiday_clean.jpg
```

### Block AI training crawlers on your website

Copy `robots.txt` to the root of your site (for example `https://example.com/robots.txt`).
Major AI companies say they respect it; it is a request, not a lock.

## Privacy checklist

Menus change over time. These are the setting names at the time of the video; check each service's official help pages.

### ChatGPT (Free, Plus, Pro)

- [ ] **Settings → Data controls → Improve the model for everyone → Off** (stops training on future chats)
- [ ] Use **Temporary Chat** for sensitive topics (not in history, no memory, not used for training; may be kept up to 30 days for safety)
- [ ] **Settings → Personalization → Memory**: review, delete or turn off
- [ ] **Settings → Data controls → Shared links**: delete old links
- [ ] **Settings → Security**: turn on multi-factor authentication
- [ ] Privacy requests: [privacy.openai.com](https://privacy.openai.com)

### Claude (Free, Pro, Max)

- [ ] **Settings → Privacy → Help improve Claude → Off** (if on, Anthropic says data may be kept up to 5 years)
- [ ] Use **Incognito chat** for sensitive topics (not in history or memory, not used for training)
- [ ] Review the **memory** options in Settings
- [ ] Remove **connectors** (Gmail, Drive, GitHub…) you don't use
- [ ] Don't send thumbs-up / thumbs-down **feedback** on sensitive chats

### Work and developers

- Business / Team / Enterprise plans and the API are **not used for training by default** at OpenAI and Anthropic.
- Use your company's **approved** AI tool for company data. Never your personal account.

### The postcard test

Before you paste anything, ask: *"Would I write this on a postcard?"* If not: remove it, replace it with a placeholder, or don't paste it.

**Never paste:** passwords, OTPs, PINs, API keys · Aadhaar, PAN, passport, card numbers · customer or employee data · company secrets · other people's private messages.

### Already shared too much?

1. Secrets (passwords, keys): **rotate them now**
2. Delete the chat and its shared links
3. Delete anything it saved to memory
4. Turn off training for future chats
5. Send a privacy request to the company
6. Work data: tell your security / IT team

## Tests

```bash
pytest -q
```

---
📺 YouTube: **itadimaigal**, Slaves of IT. Learn. Build. Break free.
