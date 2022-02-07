from sqlalchemy.orm import Session

import models
import schemas


def get_by_id(db: Session, article_type_id: int):
    return db.query(models.ArticleTypes).filter(models.ArticleTypes.id == article_type_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ArticleTypes).offset(skip).limit(limit).all()


def create(db: Session, article_type: schemas.ArticleTypeBase):
    db_article_type = models.ArticleTypes(type=article_type.type)
    db.add(db_article_type)
    db.commit()
    db.refresh(db_article_type)
    return db_article_type


def update(db: Session, article_type_id: int, article_type: schemas.ArticleTypeBase):
    db_article_type = get_by_id(db, article_type_id)
    db_article_type.type = article_type.type
    db.commit()
    db.refresh(db_article_type)
    return db_article_type


def delete(db: Session, article_type_id: int):
    db_article_type = get_by_id(db, article_type_id)
    db.delete(db_article_type)
    db.commit()
