from pydantic import BaseModel

class NewUserRequest(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    disabled: bool = None