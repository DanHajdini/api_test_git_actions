from dotenv import load_dotenv
import os
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

load_dotenv()

argon2_hasher = Argon2Hasher(
    time_cost=3,
    memory_cost=2*16,
    parallelism=4
)

password_context = PasswordHash([argon2_hasher])

def get_pepper() -> str:
    pepper = os.getenv("APPLICATION_PEPPER", None)
    return pepper

def hash(plain_password: str) -> str:
    pepper = get_pepper()
    return password_context.hash(plain_password + pepper)

def verify_password(plain_password, hash) -> bool:
    pepper = get_pepper()
    return password_context.verify(plain_password + pepper, hash)