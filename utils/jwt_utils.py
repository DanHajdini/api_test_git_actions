
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
import jwt


load_dotenv()

def create_token(id: int, role: str) -> str:
    today = datetime.now(timezone.utc)
    return jwt.encode(payload={
        'iss': 'hajdini.be',
        'iat': today.timestamp(),
        'exp': timedelta(minutes=15) + today,
        'role': role,
        'sub': str(id)
    }, key=os.getenv("SECRET_JWT"), algorithm="HS256")

def verify_token(token: str) -> dict:
    try:
        jwt.decode(token, key=os.getenv("SECRET_JWT"), algorithms=["HS256"])
    except jwt.exceptions.DecodeError as e:
        raise ValueError(e) from e
