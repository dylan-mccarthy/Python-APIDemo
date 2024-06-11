from fastapi import APIRouter, Request
from app.schemas import UserDetails

router = APIRouter()

username = None


@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@router.get("/hello")
def say_hello_default():
    # Say hello only if the username is set
    if not username:
        return {"message": "Set a username first!"}
    return {"message": f"Hello {username}"}

@router.post("/hello/")
def set_username(userDetails: UserDetails):
    global username
    username = userDetails.username
    return {"message": f"Username set to {userDetails.username}"}