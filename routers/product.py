from fastapi import APIRouter
from authentication import oauth2
import database, models 
from schemas import product as product_schema,user as user_schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from cruds import product

router = APIRouter(
    prefix="/product",
    tags=['Product']
)

get_db = database.get_db


@router.post('/', response_model=product_schema.ShowProduct)
def create_product(request: product_schema.AddProduct,db: Session = Depends(get_db), current_user: user_schema.SignUp = Depends(oauth2.get_current_user)):
    return product.create(request,db)

@router.get('/{id}',response_model=product_schema.ShowProduct)
def get_product(id:int,db: Session = Depends(get_db), current_user: user_schema.SignUp = Depends(oauth2.get_current_user)):
    return product.show(id,db)