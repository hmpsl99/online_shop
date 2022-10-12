from fastapi import APIRouter
import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from cruds import product

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.SignUp,db: Session = Depends(get_db)):
    return product.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db), current_user: schemas.SignUp = Depends(oauth2.get_current_user)):
    return product.show(id,db)