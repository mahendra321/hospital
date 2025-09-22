from passlib.context import CryptContext

password_crypt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hashing(password):
    return password_crypt.hash(password)

def verification(password,hashed_password):
    return password_crypt.verify(password,hashed_password)