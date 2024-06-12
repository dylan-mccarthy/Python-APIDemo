from pydantic import BaseModel

class UserDetails(BaseModel):
    username: str
    disabled: bool = None