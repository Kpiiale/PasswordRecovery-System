# app.py
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from services import EmailNotificationService, INotificationService
from repositories import UserRepository

# --- 1. Inicialización y Configuración ---
load_dotenv()
app = Flask(__name__)

# --- 2. Inyección de Dependencias ---
user_repository = UserRepository(db_path="users.json")
notification_service: INotificationService = EmailNotificationService()

# --- 3. Endpoints de la API (Comunicación) ---
@app.route("/health", methods=["GET"])
def health_check():
    """Endpoint de 'health check' para observabilidad y operación."""
    return jsonify({"status": "healthy"}), 200

@app.route("/api/recover-password", methods=["POST"])
def recover_password():
    """
    Endpoint principal para la recuperación de contraseña.
    Espera un JSON con solo el campo 'email'.
    """
    data = request.get_json()
    if not data or "email" not in data:
        return jsonify({"error": "Petición inválida. Se requiere 'email'."}), 400

    email = data["email"]

    # --- Lógica de Negocio Orquestada ---
    # 1. Buscar usuario (ya no hay paso de CAPTCHA)
    user = user_repository.find_by_email(email)

    if user:
        # 2. Si el usuario existe, intentar enviar notificación
        try:
            password = user.get("password")
            notification_service.send_recovery_notification(email, password)
        except ConnectionError as e:
            print(f"CRITICAL: El servicio de notificaciones falló. Error: {str(e)}")
            return jsonify({"error": "No se pudo procesar la solicitud. Intente más tarde."}), 503

    # 3. Respuesta genérica por seguridad
    return jsonify({"message": "Si tu correo está en nuestro sistema, recibirás un email de recuperación."}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)