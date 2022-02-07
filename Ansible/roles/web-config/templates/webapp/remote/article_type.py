from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import schemas
from database import SessionLocal
from services import article_type_service

app = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/article-types/{article_type_id}", response_model=schemas.ArticleType)
def read_article_type(article_type_id: int, db: Session = Depends(get_db)):
    db_article = article_type_service.get_by_id(db, article_type_id=article_type_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article type not found")
    return db_article


@app.get("/article-types")
def read_article_types(db: Session = Depends(get_db)):
    return article_type_service.get_all(db)


@app.post("/article-types", response_model=schemas.ArticleType)
def create_article_type(article_type: schemas.ArticleTypeBase, db: Session = Depends(get_db)):
    return article_type_service.create(db=db, article_type=article_type)


@app.put("/article-types/{article_type_id}", response_model=schemas.ArticleType)
def update_article_type(article_type_id: int, article_type: schemas.ArticleTypeBase, db: Session = Depends(get_db)):
    db_article_type = article_type_service.get_by_id(db, article_type_id=article_type_id)
    if db_article_type is None:
        raise HTTPException(status_code=404, detail="Article type type found")
    return article_type_service.update(db=db, article_type_id=article_type_id, article_type=article_type)


@app.delete("/article-types/{article_type_id}", response_model=schemas.ArticleType)
def delete_article_type(article_type_id: int, db: Session = Depends(get_db)):
    db_author = article_type_service.get_by_id(db, article_type_id=article_type_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Article type type found")
    return article_type_service.delete(db=db, article_type_id=article_type_id)
