from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


class Hash:
    @staticmethod
    def hash_password(password: str) -> str:
        return password_hash.hash(password)

    @staticmethod
    def verify_password(hashed_password: str, plain_password: str) -> bool:
        return password_hash.verify(plain_password, hashed_password)
