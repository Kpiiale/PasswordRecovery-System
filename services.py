import os
import smtplib
from email.mime.text import MIMEText
from abc import ABC, abstractmethod

#Clase Abstracta
class INotificationService(ABC):
    """Interfaz para cualquier servicio de notificación."""
    @abstractmethod
    def send_recovery_notification(self, to_email: str, password: str):
        pass

class EmailNotificationService(INotificationService):
    """Implementación del servicio de notificación que envía correos electrónicos."""
    def __init__(self):
        self.sender = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("EMAIL_PASSWORD")
        if not self.sender or not self.password:
            raise ValueError("Las credenciales de correo (EMAIL_SENDER, EMAIL_PASSWORD) no están configuradas.")

    def send_recovery_notification(self, to_email: str, password: str):
        subject = "Recuperación de tu Contraseña"
        body = f"Hola,\n\nHas solicitado recuperar tu contraseña. Tu contraseña es: {password}"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = to_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender, self.password)
                server.send_message(msg)
        except Exception as e:
            print(f"ERROR: Fallo al enviar correo a {to_email}. Causa: {e}")
            raise ConnectionError("El servicio de correo no está disponible.")