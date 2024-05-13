from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate


class User(BaseUser):
    username: str
    pass

class UserCreate(BaseUserCreate):
    username: str
    pass

class UserRead(BaseUserUpdate):
    username: str
    pass