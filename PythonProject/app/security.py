import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del .env

KEY = os.getenv("SECRET_KEY")
if not KEY:
    raise ValueError("SECRET_KEY no está definida en .env")

cipher = Fernet(KEY.encode())

def encrypt_password(password: str) -> str:
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str) -> str:
    return cipher.decrypt(encrypted_password.encode()).decode()
