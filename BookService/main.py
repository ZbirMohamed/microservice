from fastapi import FastAPI , Depends
from sqlalchemy import select       
from sqlalchemy.orm import Session , joinedload
from models import Author , Book
from database import get_db
from schemas import CreateAuthor, UpdateAuthor, CreateBook, UpdateBook

app = FastAPI()


@app.get('/author')
async def get_Authors(db:Session=Depends(get_db)):
    stmt = select(Author)##this select all authors
    data = db.execute(stmt).scalars().all()
    return {"Message":data}

@app.get('/author/{id}')
async def get_Author(id:int , db:Session=Depends(get_db)):
    stmt = select(Author).where(Author.id == id)
    data = db.execute(stmt).scalar_one_or_none()
    return {'Author':data}

@app.post('/author')
async def add_Authors(author:CreateAuthor,db:Session=Depends(get_db)):
    new_author = Author(**author.dict())
    db.add(new_author)
    db.commit()
    return {"Author":author}

@app.put('/author/{id}')
async def update_Authors(id:int,author:UpdateAuthor,db:Session=Depends(get_db)):
    stmt = select(Author).where(Author.id == id)
    result = db.execute(stmt).scalar_one_or_none() #returns one or none

    if not result:
        return {'Message':f'Author with id: {id} not found'}
    
    author_data = author.dict(exclude_unset=True)
    for key , value in author_data.items():
        setattr(result,key,value)
    
    db.commit()
    db.refresh(result)##gets the new values of the following author
    return {'author':result}

@app.delete('/author/{id}')
async def delete_Authors(id:int,db:Session=Depends(get_db)):
    stmt = select(Author).where(Author.id == id)
    result = db.execute(stmt).scalar_one_or_none()

    if not result:
        return {'Message':f'Author with id:{id} not found'}

    db.delete(result)
    db.commit()
    return {'Message':f'Author {id} deleted'}

######################################## Books ############################################

@app.get('/books')
async def get_books(db:Session=Depends(get_db)):
    stmt = select(Book).options(joinedload(Book.author))
    result = db.execute(stmt).scalars().all()
    return {'books':result}

@app.get('/books/{id}')
async def get_book(isbn:str,db:Session=Depends(get_db)):
    stmt = select(Book).where(Book.isbn == isbn)
    resutl = db.execute(stmt).scalar_one_or_none()

    if not resutl:
        return {'Message':f'Book with isbn:{isbn} not found'}

    return {'book':resutl}

@app.post('/books')
async def create_book(book:CreateBook,db:Session=Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    return {'Book':book}

@app.put('/books/{id}')
async def update_book(isbn:str,book:UpdateBook,db:Session=Depends(get_db)):
    stmt = select(Book).where(Book.isbn == isbn)
    result = db.execute().scalar_one_or_none()

    if not result:
        return {'Message':f'Book with isbn:{isbn} is not found'}
    book_data = book.dict(exclude_unset=True)
    for key,value in book_data.items():
        setattr(result,key,value)
    db.commit()
    db.refresh()
    return {'Book':book}

@app.delete('/books/{id}')
async def delete_book(isbn:str,db:Session=Depends(get_db)):
    stmt = select(Book).where(Book.isbn == isbn)
    result = db.execute().scalar_one_or_none()

    if not result:
        return {'Message': f'Book with isbn:{isbn} is not found'}

    db.delete(result)
    db.commit()
    return {'Message':f'Book with isbn:{isbn} is deleted'}