from secretbox_crypto import generate_key, load_key, encrypt, decrypt


# 1. Génération clé
key = generate_key()
print("KEY:", key)

# 2. Chargement clé
box = load_key(key)

# 3. Message test
message = "Message top secret atelier"
print("Original:", message)

# 4. Chiffrement
encrypted = encrypt(box, message)
print("Encrypted:", encrypted)

# 5. Déchiffrement
decrypted = decrypt(box, encrypted)
print("Decrypted:", decrypted)