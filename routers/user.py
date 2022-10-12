from fastapi import APIRouter
from authentication import oauth2
import database, schemas, models
from schemas import user as user_schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from cruds import product, user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=user_schema.ShowUser)
def create_user(request: user_schema.SignUp,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=user_schema.ShowUser)
def get_user(id:int,db: Session = Depends(get_db), current_user: user_schema.SignUp = Depends(oauth2.get_current_user)):
    return user.show(id,db)