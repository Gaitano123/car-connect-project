from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey


engine = create_engine('sqlite:///project.db')
Session = sessionmaker( bind = engine)
session = Session()


Base = declarative_base()



class Garage(Base):
    __tablename__ = 'garages'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    
    car = relationship('Car', back_populates='garage')
    
    
    
class Owner(Base):
    __tablename__ = 'owners'
    
    id= Column(Integer(), primary_key=True)
    name = Column(String())
    
    car = relationship('Car', back_populates='owner')
    
    
    
class Car(Base):
    
    __tablename__ = 'cars'
    
    id = Column(Integer(), primary_key=True)
    make = Column(String())
    model = Column(String())
    year = Column(Integer())
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    garage_id = Column(Integer(), ForeignKey('garages.id'))
    
    garage = relationship("Garage", back_populates='car')
    owner = relationship('Owner', back_populates='car')
    
    