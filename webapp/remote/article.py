from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
from database import SessionLocal
from services import article_service

app = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = article_service.get_by_id(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@app.get("/articles")
def read_articles(db: Session = Depends(get_db)):
    return article_service.get_all(db)


@app.post("/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleBase, db: Session = Depends(get_db)):
    return article_service.create(db=db, article=article)


@app.put("/articles/{article_id}", response_model=schemas.Article)
def update_article(article_id: int, article: schemas.ArticleBase, db: Session = Depends(get_db)):
    db_article = article_service.get_by_id(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article_service.update(db=db, article_id=article_id, article=article)


@app.delete("/articles/{article_id}", response_model=schemas.Article)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_author = article_service.get_by_id(db, article_id=article_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article_service.delete(db=db, article_id=article_id)
