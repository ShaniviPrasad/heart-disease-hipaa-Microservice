# security.py
from cryptography.fernet import Fernet
import os

def load_or_generate_key():
    key_file_path = "secret.key"
    
    if not os.path.exists(key_file_path):
        key = Fernet.generate_key()
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
        print("🔑 New Secret Key generated and saved to 'secret.key'")
    else:
        with open(key_file_path, "rb") as key_file:
            key = key_file.read()
        print("🔑 Existing Secret Key loaded successfully.")
        
    return Fernet(key)

# Global Encryption/Decryption Object
cipher = load_or_generate_key()

def encrypt_data(plain_text: str) -> str:
    encrypted_bytes = cipher.encrypt(plain_text.encode())
    return encrypted_bytes.decode()

def decrypt_data(cipher_text: str) -> str:
    decrypted_bytes = cipher.decrypt(cipher_text.encode())
    return decrypted_bytes.decode()

# Testing Execution
if __name__ == "__main__":
    test_patient = "Patient_Rahul_Sharma_9921"
    
    print(f"\n1. Original Identity : {test_patient}")
    
    # Encrypt
    encrypted = encrypt_data(test_patient)
    print(f"2. Encrypted Format  : {encrypted}")
    
    # Decrypt
    decrypted = decrypt_data(encrypted)
    print(f"3. Decrypted Format  : {decrypted}")