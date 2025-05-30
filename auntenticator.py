from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import pyotp
import time
import os
import json

class AuthenticatorWidget(BoxLayout):
    secrets_file = "secrets.json"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.service_input = TextInput(
            hint_text="Enter service name (e.g., Google, GitHub)",
            multiline=False,
            font_size=18,
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.service_input)

        self.secret_input = TextInput(
            hint_text="Enter your TOTP secret (Base32)",
            multiline=False,
            font_size=18,
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.secret_input)

        self.generate_button = Button(
            text="Generate OTP",
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.86, 1),
            font_size=20
        )
        self.generate_button.bind(on_press=self.start)
        self.add_widget(self.generate_button)

        self.otp_label = Label(
            text="OTP will appear here",
            font_size=48,
            size_hint=(1, None),
            height=100,
            bold=True
        )
        self.add_widget(self.otp_label)

        self.timer_label = Label(
            text="",
            font_size=24,
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.timer_label)

        self.totp = None
        self.event = None

        self.load_last_secret()

    def load_secrets(self):
        if os.path.exists(self.secrets_file):
            with open(self.secrets_file, "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
                except:
                    pass
        return []

    def save_secrets(self, secrets):
        with open(self.secrets_file, "w") as f:
            json.dump(secrets, f, indent=4)

    def load_last_secret(self):
        secrets = self.load_secrets()
        if secrets:
            # Load the last saved secret and service
            last = secrets[-1]
            self.service_input.text = last.get("service", "")
            self.secret_input.text = last.get("secret", "")

    def start(self, instance):
        service = self.service_input.text.strip()
        secret = self.secret_input.text.strip()

        if not service:
            self.otp_label.text = "[color=ff0000]Please enter a service name![/color]"
            return
        if not secret:
            self.otp_label.text = "[color=ff0000]Please enter a secret![/color]"
            return
        try:
            self.totp = pyotp.TOTP(secret)
            _ = self.totp.now()
        except Exception:
            self.otp_label.text = "[color=ff0000]Invalid secret![/color]"
            return

        # Load current secrets list
        secrets = self.load_secrets()

        # Check if service exists, update secret if yes
        for entry in secrets:
            if entry["service"].lower() == service.lower():
                entry["secret"] = secret
                break
        else:
            # Add new entry
            secrets.append({"service": service, "secret": secret})
            
        # Before saving, check if this secret already exists for another service
        for entry in secrets:
            if entry["secret"] == secret and entry["service"].lower() != service.lower():
                self.otp_label.text = "[color=ff0000]Secret already used by another service![/color]"
                return


        self.save_secrets(secrets)

        self.update_otp(0)
        if self.event:
            self.event.cancel()
        self.event = Clock.schedule_interval(self.update_otp, 1)

    def update_otp(self, dt):
        if not self.totp:
            return
        current_otp = self.totp.now()
        self.otp_label.text = current_otp

        time_left = 30 - (int(time.time()) % 30)
        self.timer_label.text = f"Next code in: {time_left:02d}s"


class AuthenticatorApp(App):
    def build(self):
        return AuthenticatorWidget()


if __name__ == '__main__':
    AuthenticatorApp().run()
