from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey


engine = create_engine('sqlite:///project.db')
Base = declarative_base()







if __name__ == '__main__':
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker( bind = engine)
    session = Session()