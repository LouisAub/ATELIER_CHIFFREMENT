from nacl.secret import SecretBox
from nacl.utils import random
import base64


# Génération d’une clé (32 bytes)
def generate_key():
    key = random(SecretBox.KEY_SIZE)
    return base64.b64encode(key).decode()


# Charger une clé depuis base64
def load_key(key_b64: str):
    key = base64.b64decode(key_b64)
    return SecretBox(key)


# Chiffrement
def encrypt(box: SecretBox, message: str) -> str:
    encrypted = box.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()


# Déchiffrement
def decrypt(box: SecretBox, token_b64: str) -> str:
    token = base64.b64decode(token_b64)
    decrypted = box.decrypt(token)
    return decrypted.decode()