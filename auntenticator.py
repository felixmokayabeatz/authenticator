import tkinter as tk
from tkinter import messagebox
import pyotp
import time

class AuthenticatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Authenticator")

        self.secret_var = tk.StringVar()
        self.otp_var = tk.StringVar(value="Enter secret and press Generate")
        self.timer_var = tk.StringVar(value="")

        tk.Label(root, text="Enter your TOTP secret (Base32):").pack(pady=5)
        tk.Entry(root, textvariable=self.secret_var, width=40).pack(pady=5)

        tk.Button(root, text="Generate OTP", command=self.start).pack(pady=10)

        tk.Label(root, text="Current OTP:", font=("Helvetica", 14)).pack(pady=(20,5))
        tk.Label(root, textvariable=self.otp_var, font=("Helvetica", 24, "bold")).pack()

        tk.Label(root, textvariable=self.timer_var, font=("Helvetica", 12)).pack(pady=10)

        self.totp = None
        self.countdown_seconds = 30
        self.running = False

    def start(self):
        secret = self.secret_var.get().strip()
        if not secret:
            messagebox.showerror("Error", "Please enter a secret!")
            return
        try:
            self.totp = pyotp.TOTP(secret)
            # Test generate to validate secret, throws exception if invalid
            self.totp.now()
        except Exception as e:
            messagebox.showerror("Error", "Invalid secret!")
            return

        if not self.running:
            self.running = True
            self.update_otp()

    def update_otp(self):
        if not self.running:
            return

        current_otp = self.totp.now()
        self.otp_var.set(current_otp)

        # Countdown timer starts at 30 and goes down
        self.countdown_seconds = 30
        self.update_timer()

    def update_timer(self):
        if self.countdown_seconds >= 0:
            mins, secs = divmod(self.countdown_seconds, 60)
            self.timer_var.set(f"Next code in: {mins:02d}:{secs:02d}")
            self.countdown_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.update_otp()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthenticatorApp(root)
    root.mainloop()
