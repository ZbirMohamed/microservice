from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from models import Author, Book
from schemas import CreateAuthor, UpdateAuthor, CreateBook, UpdateBook


############################ AUTHOR CRUD ################################
def get_authors(db: Session):
    stmt = select(Author)
    authors = db.execute(stmt).scalars().all()
    return authors

def get_author(id: int , db: Session):
    stmt = select(Author).where(Author.id == id)
    author = db.execute(stmt).scalar_one_or_none() ## le resultat est None ou un objet
    return author

def add_auhtor(author: CreateAuthor, db: Session):
    demannde = Author(**author.dict())
    db.add(demannde)
    db.commit()
    return author

def update_author(id: int ,author:UpdateAuthor ,db: Session):
    stmt = select(Author).where(Author.id == id)
    update_author = db.execute(stmt).scalar_one_or_none()

    if not author:
        return False

    for key , val in author.dict().items():
        setattr(update_author, key, val)

    db.commit()
    return author

def delete_author(id: int , db: Session):
    stmt = select(Author).where(Author.id == id)
    author = db.execute(stmt).scalar_one_or_none()

    if not author:
        return False

    db.delete(author)
    db.commit()
    return True



##################################### CRUD BOOKS ######################################
def get_books(db:Session):
    stmt = select(Book).options(joinedload(Book.author)) ## ceci ajoute la relation entre les livres et les auteurs
    books = db.execute(stmt).scalars().all()
    return books

def get_book_by_id(id: str , db: Session):
    stmt = select(Book).where(Book.isbn == id).options(joinedload(Book.author))
    book = db.execute(stmt).scalar_one_or_none()
    return book

def add_book(book:CreateBook,db:Session):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    return book

def update_book(book:UpdateBook,id:str , db:Session):
    stmt = select(Book).where(Book.isbn ==id)
    update_book = db.execute(stmt).scalar_one_or_none()

    if not update_book:
        return False

    for key,val in book.dict().items():
        setattr(update_book,key,val)

    db.commit()
    return book

def delete_book(id:str , db:Session):
    stmt = select(Book).where(Book.isbn ==id)
    book = db.execute(stmt).scalar_one_or_none()

    if not book:
        return False

    db.delete(book)
    db.commit()
    return True