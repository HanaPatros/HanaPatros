from passlib.context import CryptContext

pwt_context = CryptContext(Schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwt_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(plain_password):
        return pwt_context.hash(plain_password)