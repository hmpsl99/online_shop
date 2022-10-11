from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI
import  models
from database import engine
from  routers import  user, authentication

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(authentication.router)



