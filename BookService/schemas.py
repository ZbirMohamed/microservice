from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class CreateAuthor(BaseModel):
    nom:str = Field(min_length=4, max_length=25)
    prenom: str = Field(min_length=4, max_length=25)
    dateNaissance: date

class UpdateAuthor(BaseModel):
    nom: Optional[str] = Field(None, min_length=4, max_length=25)
    prenom: Optional[str] = Field(None, min_length=4, max_length=25)
    dateNaissance: Optional[date] = None

class CreateBook(BaseModel):

    isbn :str = Field(min_length=25,max_length=25) ##Pour s'assurer que la taille d'un ISBN soit identique
    titre :str = Field(min_length=3,max_length=70)
    description :Optional[str] = Field(min_length=20)
    prix:float = Field(min_value=5,max_value=2000)
    anneeEdition:str = Field(min_length=3,max_length=4)
    author_id: int

class UpdateBook(BaseModel):

    titre: Optional[str] = Field(None,min_length=3, max_length=70)
    description: Optional[str] = Field(None,min_length=20, max_length=255)
    prix: Optional[str] = Field(None,min_value=5, max_value=2000)
    anneeEdition: Optional[str] = Field(None,min_length=3, max_length=4)
    author_id: Optional[str] = Field(None)

class Author(BaseModel):

    id:int
    nom: str
    prenom: str
    dateNaissance: date

    class Config:
        from_attributes = True

class Book(BaseModel):

    isbn: str
    titre: str
    description: Optional[str]
    prix: float
    anneeEdition: str
    author_id: int