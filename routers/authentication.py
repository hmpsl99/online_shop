from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import  database, models
from authentication import tokenn
from schemas import product as product_schema, user as user_schema
from authentication import hashing
from sqlalchemy.orm import Session


router = APIRouter(prefix='/login',tags=['Authentication'])

@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = tokenn.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}