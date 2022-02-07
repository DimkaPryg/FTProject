from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import schemas
from database import SessionLocal
from services import author_service

app = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = author_service.get_by_id(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.get("/authors")
def read_authors(db: Session = Depends(get_db)):
    return author_service.get_all(db)


@app.post("/authors", response_model=schemas.Author)
def create_author(author: schemas.AuthorBase, db: Session = Depends(get_db)):
    return author_service.create(db=db, author=author)


@app.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author: schemas.AuthorBase, db: Session = Depends(get_db)):
    db_author = author_service.get_by_id(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author_service.update(db=db, author_id=author_id, author=author)


@app.delete("/authors/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = author_service.get_by_id(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author_service.delete(db=db, author_id=author_id)