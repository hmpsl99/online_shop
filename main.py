from pydoc import ModuleScanner
from pyexpat import model
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from online_shop import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()