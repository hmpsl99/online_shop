from fastapi import APIRouter
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from cruds import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.SignUp,db: Session = Depends(get_db)):
    return user.create(request,db)