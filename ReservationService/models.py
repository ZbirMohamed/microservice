from sqlalchemy import Column, String, Integer , Date , Boolean
from database import Base
import datetime


################## Models #########################

class Reservation(Base):

    __tablename__ = 'Reservations'

    id = Column(Integer, primary_key=True,index=True) # Coulumn == ligne(champs) , primary_key = true == cle primaire , index = champs indexe
    user_id = Column(String(25), nullable=False) #String(25)  == varchar(25)
    book_id = Column(String(25), nullable=False)
    dateReservation = Column(Date, default=datetime.date.today(),nullable=False)#Date = date
    dateRetour = Column(Date, default=datetime.date.today(),nullable=False)#Date = date
    isReturned = Column(Boolean,default=False)