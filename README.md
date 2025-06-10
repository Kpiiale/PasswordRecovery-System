# PasswordRecovery-System
Un microservicio que gestiona el proceso de recuperación de contraseñas de los usuarios.

-  Se enfoca exclusivamente en la recuperación de contraseñas, sin mezclar otras responsabilidades como registro o autenticación.
-  Utiliza una clase abstracta (`INotificationService`) para definir un contrato de notificación. Esto permite cambiar fácilmente la implementación (por ejemplo, de email a SMS) sin alterar la lógica de negocio principal.
-   Las dependencias (como el servicio de notificaciones) se "inyectan" en el punto de entrada de la aplicación.
-  Los datos sensibles (credenciales de correo) se manejan fuera del código fuente, a través de un archivo `.env`\
-  El servicio gestiona su propio almacén de datos (`users.json`), el cual no debe ser accedido directamente por ningún otro servicio del ecosistema.

Esta pensado para ser usado con una base de datos, sin embargo, como prueba se usa un json. 

---

### Ejecución Local con Entorno Virtual (`venv`)

**Pasos:**

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2.  **Crear y activar el entorno virtual:**
    ```bash
    # Crear el venv (solo una vez)
    python -m venv venv

    # Activar el venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crear el archivo de configuración (`.env`):**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tus credenciales de correo:
    ```ini
    EMAIL_SENDER="tu_correo@gmail.com"
    EMAIL_PASSWORD="tu_contrasena_de_aplicacion"
    ```

5.  **Iniciar el servidor:**
    ```bash
    flask --app app run --port 5001
    ```

### Prueba de funcionamiento 
En users.json cambia el email por uno de tu preferencia (Debe ser válido para recibir el correo)

Instala la extensión REST Client-Huachao Mao para el endpoint que verifica que el servicio está activo y saludable 

En el archico test-api.htttp reeemplaza usuario.prueba@gmail.com a un correo que se encuentre en users.json y presiona Send Request. 