import os
import hashlib
from fastapi import APIRouter
from ..encrypt_utils import encrypt
from app.schemas import LoginRequest
from app.data import get_user_by_username

router = APIRouter()

key = os.environ.get("ENCRYPTION_KEY")
if not key:
    raise ValueError("No encryption key set for the application")

hashed_key = hashlib.sha256(key.encode()).digest()


@router.post("/login/")
def login(loginRequest: LoginRequest):
    #find user in database
    user = get_user_by_username(loginRequest.username)
    if user is None:
        return {"message": "User not found"}
    
    #encrypt the password
    encrypted_password = encrypt(loginRequest.password, hashed_key)
    
    #compare the passwords
    if user.password == encrypted_password:
        return {"message": "Login successful"}
    else:
        return {"message": "Incorrect password"}
    
    
