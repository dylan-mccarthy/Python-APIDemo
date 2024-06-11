from fastapi import APIRouter
from app.models import User
from app.data import get_users

router = APIRouter()

@router.get("/users/")
def get_all_users():
    users = get_users()
    return [map_user_to_userDetails(user) for user in users]



def map_user_to_userDetails(user: User):
    return {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "disabled": user.disabled
    }