```python
from cryptography.fernet import Fernet

class CryptographicAlchemy:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_message(self, message):
        """
        This function encrypts the message using Fernet symmetric encryption.
        """
        cipher_text = self.cipher_suite.encrypt(message.encode())
        return cipher_text

    def decrypt_message(self, cipher_text):
        """
        This function decrypts the cipher text back into the original message.
        """
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def update_key(self, new_key):
        """
        This function updates the encryption key.
        """
        self.key = new_key
        self.cipher_suite = Fernet(self.key)

alchemyOfKnowledge = CryptographicAlchemy()
```