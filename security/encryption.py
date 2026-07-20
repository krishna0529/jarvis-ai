class EncryptionEngine:

    def encrypt(self, data: str) -> bytes:
        return data.encode()

    def decrypt(self, encrypted_data: bytes) -> str:
        return encrypted_data.decode()
