import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime, timedelta

oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

secret_key = "3f1ec453afb1546f428997fe5f22565c6ee8c16ee8703f35d48abbc236b794a8"
algotithm = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30


def create_access_token(data : dict):
    to_encode = data
    expire_time = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":expire_time})
    encoded_jwt = jwt.encode(to_encode,secret_key,algorithm=algotithm)
    return encoded_jwt


token = create_access_token({})
print(token)
