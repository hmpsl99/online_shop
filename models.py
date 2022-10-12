from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Column,Integer,String,DateTime
from database import  Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer,primary_key = True, index = True)
    username = Column(String, unique= True)
    email = Column(String, unique = True)
    password = Column(String)

    basket = relationship('Basket',back_populates = 'user')

class Product(Base):
    __tablename__= 'product'

    id = Column(Integer,primary_key = True, index = True)
    title = Column(String)
    price = Column(Integer)
    creation_time = Column(DateTime, default = datetime.now())

    product = relationship('BasketItem', back_populates = 'product')

class Basket(Base):
    __tablename__= 'basket'

    id = Column(Integer,primary_key = True, index = True)
    creation_time = Column(DateTime, default = datetime.now())
    user_id = Column(Integer ,ForeignKey('user.id'))

    user = relationship('User', back_populates = "basket")
    basket_item = relationship('BasketItem', back_populates = 'basket')

class BasketItem(Base):
    __tablename__= 'basket_item'

    id = Column(Integer,primary_key = True, index = True)
    creation_time = Column(DateTime, default = datetime.now())
    basket_id = Column(Integer ,ForeignKey('basket.id'))
    product_id = Column(Integer ,ForeignKey('product.id'))

    basket = relationship('Basket', back_populates = 'basket_item')
    product = relationship('Product', back_populates = 'product')




    


