from fastapi import FastAPI
from .routers import hello
from .routers import registration
from .routers import users
from .routers import login

app = FastAPI()

app.include_router(hello.router)
app.include_router(registration.router)
app.include_router(users.router)
app.include_router(login.router)