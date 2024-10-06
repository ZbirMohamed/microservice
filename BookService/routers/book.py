import sys
sys.path.append('..')
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from BookService.database import get_db
from BookService.crud import get_books ,get_book_by_id, add_book ,update_book , delete_book
from BookService.schemas import Book, CreateBook, UpdateBook


router = APIRouter(
    prefix="/book",
    tags=["book"],
    responses={404: {"description": "no book found"}}
)

@router.get("",response_model=list[Book])
async def get_all_books(db: Session = Depends(get_db)):
    books = get_books(db)
    return {"books": books }

@router.get("/{id}",response_model=Book)
async def get_book(id:str,db: Session = Depends(get_db)):
    book = get_book_by_id(id,db)
    return {"book": book}

@router.post("",response_model=Book)
async def create_book(book: CreateBook,db: Session =Depends(get_db) ):
    new_book = add_book(book,db)
    return {"book": new_book}

@router.put("/{id}",response_model=Book)
async def update_Author(id: str,book:UpdateBook,db:Session=Depends(get_db)):
    book = update_book(id,book,db)
    if not book:
        return {"message": "No author found"}
    return {"author": book}

@router.delete("/{id}")
async def delete_Author(id:str,db: Session = Depends(get_db)):
    book = delete_book(id,db)
    if not book:
        return {"message": "No author found"}
    return {'Message': f'Book with isbn:{id} is deleted'}
