from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
Base = declarative_base()
class Rating(Base):
    __tablename__="rating"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    item_id=Column(Integer)
    rating=Column(Integer)
class Products(Base):
    __tablename__= "products"
    id= Column(Integer,primary_key=True)
    name= Column(String(255))
    description= Column(String(255))
    quantity= Column(Integer)
    price= Column(Integer)
    image= Column(String(255))
    rating= Column(String(255))
class Cart(Base):
    __tablename__="cart"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    item_id=Column(Integer)
    quantity=Column(Integer)
class Comments(Base):
    __tablename__= "comments"
    id= Column(Integer,primary_key=True)
    content = Column(String(1600))
    user_id = Column(Integer)
    user_name = Column(String(255))
    item_id = Column(Integer)  
    rating = Column(Integer)
class Users(Base):
    __tablename__ = "users"
    id= Column(Integer,primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    birthday = Column(String(255))
    email = Column(String(255))
    gender = Column(String(255))
    username = Column(String(255))
    profile = Column(String(255))
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()