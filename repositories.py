import json

class UserRepository:
    """
    Repositorio para gestionar el acceso a los datos de los usuarios.
    Abstrae el origen de los datos (en este caso, un archivo JSON).
    """
    def __init__(self, db_path: str):
        self._db_path = db_path

    def find_by_email(self, email: str) -> dict | None:
        """Busca un usuario por su email y devuelve sus datos o None si no lo encuentra."""
        try:
            with open(self._db_path, 'r') as f:
                users = json.load(f)
                return users.get(email)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        
