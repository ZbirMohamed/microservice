import sys
sys.path.append('..')
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import get_authors,get_author , add_auhtor , update_author ,delete_author
from ..schemas import Author, CreateAuthor, UpdateAuthor

router = APIRouter(
    prefix="/author",
    tags=["author"],
    responses={404: {"description": "no author found"}}
)

@router.get("",response_model=list[Author])
async def get_all_authors(db: Session = Depends(get_db)):
    authors = get_authors(db)
    return {"authors": authors}

@router.get("/{id}",response_model=Author)
async def get_author_by_id(id: int,db: Session = Depends(get_db)):
    author = get_author(id,db)
    return {"author": author}

@router.post("",response_model=Author)
async def create_author(author: CreateAuthor,db: Session =Depends(get_db) ):
    author = add_auhtor(author,db)
    return {"author": author}

@router.put("/{id}",response_model=Author)
async def update_Author(id: int,author:UpdateAuthor,db:Session=Depends(get_db)):
    author = update_author(id,author,db)
    if not author:
        return {"message": "No author found"}
    return {"author": author}

@router.delete("/{id}")
async def delete_Author(id,db: Session = Depends(get_db)):
    author = delete_author(id,db)
    if not author:
        return {"message": "No author found"}
    return {'Message': f'Author {id} deleted'}
