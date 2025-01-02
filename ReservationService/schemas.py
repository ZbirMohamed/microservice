from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class CreateReservation(BaseModel):
    user_id:int = Field(min=1) 
    book_id: int = Field(min=1)
    dateReservation: date = Field(ge=date.today())
    dateRetour: date = Field(ge=date.today())
    isReturned: bool

class Reservation(BaseModel):

    user_id:int
    book_id: int
    dateReservation: date
    dateRetour: date 
    isReturned: bool

    class Config:
        from_attributes = True