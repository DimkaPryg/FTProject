from sqlalchemy.orm import Session

import models
import schemas


def get_by_id(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create(db: Session, author: schemas.AuthorBase):
    db_user = models.Author(author=author.author)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(db: Session, author_id: int, author: schemas.AuthorBase):
    db_author = get_by_id(db, author_id)
    db_author.author = author.author
    db.commit()
    db.refresh(db_author)
    return db_author


def delete(db: Session, author_id: int):
    db_author = get_by_id(db, author_id)
    db.delete(db_author)
    db.commit()
