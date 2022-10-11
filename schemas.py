from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class SignUp(BaseModel):
    username: str 
    email: str
    password: str


class Login(BaseModel):
    username: str
    password:str

class ShowUser(BaseModel):
    username: str 
    email: str

    class Config:
        orm_mode = True