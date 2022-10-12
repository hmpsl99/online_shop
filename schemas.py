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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class ShowProduct(BaseModel):
    id : int
    title : str
    price : int 
    creation_time : datetime

    class Config:
        orm_mode = True

class AddProduct(BaseModel):
    title: str
    price: int 

    
