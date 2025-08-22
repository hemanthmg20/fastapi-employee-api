from passlib.context import CryptContext

from datetime import datetime,timedelta,timezone
from typing import Optional
from jose import JWTError, jwt


pwd_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# ------ JWT ------

SECRET_KEY = "secretpasscode"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data : dict , expire_time : Optional[timedelta] = None):
    to_encode = data.copy()
    min_to_extend = datetime.now(timezone.utc) + (expire_time or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp' : min_to_extend})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token : str):
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    

