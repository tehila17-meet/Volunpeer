from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
Base = declarative_base()

class Volunteers(Base):
    __tablename__ = "volunteers"
    id= Column(Integer,primary_key=True)
    VolunteeringHours = relationship("volunteeringhours", uselist=False, backref="volunteers")
    name = Column(String(255))
    password = Column(String(255))
    birthday = Column(String(255))
    email = Column(String(255))
    gender = Column(String(255))
    username = Column(String(255))
    interests = Column(String(255))
class Organizations(Base):
    __tablename__="organizations"
    id=Column(Integer,primary_key=True)
    volunteeringhours = relationship("volunteeringhours", uselist=False,backref="organizations")
    name = Column(String(255))
    password = Column(String(255))
    creationdate = Column(String(255))
    email = Column(String(255))
    username = Column(String(255))
    decscription = Column(Strindg(1000))
    shortdescription = Column(String(300))
    fields = Column(String(255))
class VolunteeringHours(Base):
    __tablename__="volunteeringhours"
    id=Column(Integer,primary_key=True)
    volunteer_id= Column(Integer, ForeignKey('volunteers.id'))
    hours =Column(Integer)
    organization_id= Column(Integer,ForeignKey('organizations.id'))
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()