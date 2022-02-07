from sqlalchemy.orm import Session

import models
import schemas


def get_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()


def create(db: Session, article: schemas.ArticleBase):
    db_article = models.Article(magazine_id=article.magazine_id,
                                article_type_id=article.article_type_id,
                                author_id=article.author_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update(db: Session, article_id: int, article: schemas.ArticleBase):
    db_article = get_by_id(db, article_id)
    db_article.magazine_id = article.magazine_id
    db_article.article_type_id = article.article_type_id
    db_article.author_id = article.author_id
    db.commit()
    db.refresh(db_article)
    return db_article


def delete(db: Session, article_id: int):
    db_article = get_by_id(db, article_id)
    db.delete(db_article)
    db.commit()

