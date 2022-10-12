from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


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