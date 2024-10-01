from fastapi import FastAPI , Depends
from sqlalchemy import select       
from sqlalchemy.orm import Session       
from models import Author
from database import get_db
from schemas import CreateAuthor, UpdateAuthor


app = FastAPI()


@app.get('/')
async def get_Authors(db:Session=Depends(get_db)):
    stmt = select(Author)##this select all authors
    data = db.execute(stmt).scalars().all()
    return {"Message":data}

@app.get('/{id}')
async def get_Author(id:int , db:Session=Depends(get_db)):
    stmt = select(Author).where(Author.id == id)
    data = db.execute(stmt).scalar_one_or_none()
    return {'Author':data}

@app.post('/')
async def add_Authors(author:CreateAuthor,db:Session=Depends(get_db)):
    new_author = Author(**author.dict())
    db.add(new_author)
    db.commit()
    return {"Author":author}

@app.put('/{id}')
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

@app.delete('/{id}')
async def delete_Authors(id:int,db:Session=Depends(get_db)):
    stmt = select(Author).where(Author.id == id)
    result = db.execute(stmt).scalar_one_or_none()

    if not result:
        return {'Message':f'Author with id:{id} not found'}

    db.delete(result)
    db.commit()
    return {'Message':f'Author {id} deleted'}