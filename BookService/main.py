from fastapi import FastAPI
from routers import author,book

app = FastAPI()


app.include_router(author.router)
app.include_router(book.router)
