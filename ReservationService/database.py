from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqlAlchemyUrl = "mysql+pymysql://root:@localhost:3306/reservationDB"

engine = create_engine(sqlAlchemyUrl)

LocalSession = sessionmaker(bind=engine,autocommit= False,autoflush=False)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()
