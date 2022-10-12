from sqlalchemy.orm import Session
from schemas import  product as product_schema
import models
from fastapi import HTTPException,status

def create(request: product_schema.AddProduct,db:Session):
    new_product = models.Product(title=request.title,price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def show(id:int,db:Session):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with the id {id} is not available")
    return product