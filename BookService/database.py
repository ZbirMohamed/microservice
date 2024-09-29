from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlAlchemyUrl = "mysql+pymysql://root:Dracaufeu339@localhost:3306/booksDB"

engine = create_engine(sqlAlchemyUrl)

LocalSession = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()
