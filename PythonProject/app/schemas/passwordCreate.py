from pydantic import BaseModel

class PasswordCreate(BaseModel):
    service: str
    username: str
    password: str