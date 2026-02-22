# 🔐 Authenticator
A simple **TOTP (Time-based One-Time Password)** authenticator app built with **Python** and **Kivy** for generating secure 2-factor authentication (2FA) codes locally on your computer.
This application allows you to generate login verification codes (for services like GitHub, Google, and others) without relying on a mobile device.

---

## ✨ Features
- 🔐 Generate TOTP codes for 2FA-enabled accounts
- 🗃️ Store secrets locally on the device
- ⚡ Automatic OTP refresh every 30 seconds
- 🖥️ Cross-platform desktop application
- 🐍 Built using Python and Kivy
- 💾 Remembers previously added services

---

## 📸 Screenshot
![Authenticator Screenshot](screenshort/one.png)

---

## 📦 Requirements
- Python 3.11 (recommended for Kivy compatibility)
- pip (Python package manager)

> ⚠️ Newer Python versions (3.13/3.14) may not yet fully support Kivy.

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/mosesamwoma/authenticator.git
```

**2. Navigate into the project directory**
```bash
cd authenticator
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:
```bash
python auntenticator.py
```

### Steps
1. Enter a service name (e.g., GitHub, Google)
2. Paste your TOTP secret key (Base32 format)
3. Click **Generate OTP**
4. A new authentication code will appear and refresh every 30 seconds

---

## 💻 Desktop App (Windows)

Prefer not to set up Python? Download the ready-to-run Windows executable directly:

**[⬇️ Download Authenticator.exe](https://github.com/mosesamwoma/authenticator/releases/download/untagged-17b79d5d300c9a85a32b/Authenticator.exe)**

Just download and run — no Python installation required!

---

## ⚙️ How It Works

TOTP (Time-based One-Time Password) generates temporary authentication codes using:
- A shared secret key
- The current system time

Each code:
- Expires every 30 seconds
- Can only be used once
- Adds an extra layer of account security

The app uses the `pyotp` library to implement the TOTP standard (RFC 6238).

---

## 🔒 Security Note

Secrets are stored locally in a JSON file on your device. They are not uploaded or shared externally.

> Future improvements may include encryption for enhanced protection.

---

## 🛠️ Built With
- [Python](https://www.python.org/)
- [Kivy](https://kivy.org/)
- [PyOTP](https://pyauth.github.io/pyotp/)

---

## 🙌 Contributions

Contributions, suggestions, and improvements are welcome!
Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
