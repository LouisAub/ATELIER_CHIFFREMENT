import os
import sys
from cryptography.fernet import Fernet


def get_key():
    """
    Récupère la clé depuis GitHub Secrets via variable d'environnement FERNET_KEY.
    """
    key = os.getenv("FERNET_KEY")

    if not key:
        print("❌ ERREUR : clé FERNET_KEY absente")
        print("👉 Elle doit être configurée via GitHub Secrets ou export FERNET_KEY")
        sys.exit(1)

    print("🔐 Clé chargée depuis GitHub Secret (FERNET_KEY)")
    return key.encode()


def encrypt_file(fernet, input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"✔ Chiffrement réussi (GitHub Secret utilisé) : {output_file}")


def decrypt_file(fernet, input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print(f"✔ Déchiffrement réussi (GitHub Secret utilisé) : {output_file}")


def main():
    if len(sys.argv) != 4:
        print("Usage :")
        print("  python fernet_atelier1.py encrypt input.txt output.enc")
        print("  python fernet_atelier1.py decrypt input.enc output.txt")
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    key = get_key()
    fernet = Fernet(key)

    if action == "encrypt":
        encrypt_file(fernet, input_file, output_file)
    elif action == "decrypt":
        decrypt_file(fernet, input_file, output_file)
    else:
        print("❌ Action invalide")
        sys.exit(1)


if __name__ == "__main__":
    main()