from fastapi import FastAPI, Depends
from app.db import create_db_and_tables
from app.schemas import UserUpdate, UserCreate, UserRead, User
from app.users import fastapi_users, active_user, fastapi_users, auth_backend
import os

app = FastAPI()
app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["auth"])
app.add_api_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), tags=["auth"])
app.include_router(fastapi_users.get_verify_router(UserRead), tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), tags=["users"], prefix="/users")

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(active_user)):
    return {f"message": "Hello from {user.username} mit {user.email}"}



@app.on_event("startup")
async def startup():
    await create_db_and_tables()


@app.on_event("shutdown")
async def shutdown():
    os.remove("test.db")