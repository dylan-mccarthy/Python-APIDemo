#Registration router for getting new users to register
import os
import hashlib
from fastapi import APIRouter
from ..encrypt_utils import encrypt
from app.schemas import NewUserRequest
from app.models import User
from app.data import add_user

router = APIRouter()

key = os.environ.get("ENCRYPTION_KEY")
if not key:
    raise ValueError("No encryption key set for the application")

hashed_key = hashlib.sha256(key.encode()).digest()

#Register a new user, encrypt the password securely
@router.post("/register/")
def register_user(newUserRequest: NewUserRequest):
    #encrypt the password
    encrypted_password = encrypt(newUserRequest.password, hashed_key)
    newUser = User(username=newUserRequest.username, email=newUserRequest.email, full_name=newUserRequest.full_name, password=encrypted_password, disabled=newUserRequest.disabled)
    add_user(newUser)
    
    
