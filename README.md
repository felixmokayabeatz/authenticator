# Authenticator

A simple TOTP (Time-based One-Time Password) authenticator app built with Python and Kivy for generating secure 2-factor authentication codes. Secrets are stored locally in a secure way. This app helps you generate one-time login codes (e.g., for GitHub, Google, etc.) without needing another device.

## Features

* 🔐 Generate TOTP codes for 2FA-enabled accounts
* 🗃️ Store secrets securely on the device
* 🐍 Python + Kivy UI — runs cross-platform
* ⚡ Lightweight and simple to use

## Requirements

* Python 3.x
* Kivy (Python UI framework)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mosesamwoma/authenticator.git
```

2. Navigate into the project:
```bash
cd authenticator
```

3. Install dependencies:
```bash
pip install kivy
```

## Usage

Run the app with:
```bash
python auntenticator.py
```

Then follow the UI prompts to add a TOTP secret and generate corresponding codes.

## How It Works

TOTP generates time-based codes that expire every 30 seconds, providing an extra layer of security for your accounts. Simply scan a QR code or manually enter your secret key, and the app will generate valid authentication codes.

## License

This project is a fork of [felixmokayabeatz/authenticator](https://github.com/felixmokayabeatz/authenticator).

---
