# AUTHENTICATOR

> Generate secure 2FA codes — locally, instantly, privately.

A lightweight TOTP (Time-based One-Time Password) authenticator built with Python and Kivy. No phone needed. No cloud. Just you and your codes.

---

## What It Does

Authenticator generates login verification codes for any 2FA-enabled service — GitHub, Google, and beyond — directly on your desktop. Fast, offline, and fully under your control.

---

## Features

- **TOTP Code Generation** — Industry-standard 2FA codes on demand
- **Local Secret Storage** — Your keys never leave your machine
- **Auto-Refresh** — Codes rotate every 30 seconds automatically
- **Cross-Platform** — Runs on any desktop via Python + Kivy
- **Persistent Memory** — Remembers every service you add

---

## Screenshot

![Authenticator Screenshot](screenshort/picture.png)

---

## Requirements

- Python 3.11 *(recommended — newer versions may have Kivy compatibility issues)*
- pip

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/mosesamwoma/authenticator.git

# 2. Enter the directory
cd authenticator

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch
python auntenticator.py
```

---

## How to Use

1. Enter a **service name** (e.g. GitHub, Google)
2. Paste your **TOTP secret key** (Base32 format)
3. Hit **Generate OTP**
4. Your code appears — and refreshes every 30 seconds

---

## Windows Executable

Don't want to deal with Python? Just grab the `.exe`:

**[⬇ Download Authenticator.exe](https://github.com/mosesamwoma/authenticator/releases/download/untagged-17b79d5d300c9a85a32b/Authenticator.exe)**

Download. Double-click. Done.

---

## How It Works

TOTP codes are generated using two inputs: a shared secret key + the current time. Each code:

- Expires after **30 seconds**
- Is valid for **one use only**
- Adds a real layer of account security

Built on `pyotp`, implementing the TOTP standard (RFC 6238).

---

## Security

Secrets are stored in a local JSON file on your device — never uploaded, never shared.

> Encryption for stored secrets is planned for a future release.

---

## Roadmap

| # | Feature | Status |
|---|---------|--------|
| 1 | Encrypt stored secrets | Planned |
| 2 | App lock / PIN | Planned |
| 3 | Multi-account dashboard | Planned |
| 4 | One-click OTP copy | Planned |
| 5 | QR code scanning | Planned |
| 6 | Edit / delete accounts | Planned |
| 7 | Countdown progress bar | Planned |
| 8 | Dark mode UI | Planned |
| 9 | Service icons | Planned |
| 10 | Windows installer (.exe setup) | Planned |
| 11 | Auto-update system | Planned |
| 12 | Backup & restore accounts | Planned |
| 13 | Master password unlock | Planned |
| 14 | Chrome extension | Planned |
| 15 | Mobile app (Android / iOS) | Planned |
| 16 | GitHub Actions CI/CD | Planned |

---

## Built With

- [Python](https://www.python.org/)
- [Kivy](https://kivy.org/)
- [PyOTP](https://pyauth.github.io/pyotp/)

---

## Contributing

Pull requests are welcome. Fork the repo, make your changes, and submit a PR. Suggestions and issues are always open.

---

## Support

If this project helped you, a ⭐ on GitHub goes a long way.