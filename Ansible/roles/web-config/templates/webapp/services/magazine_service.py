from sqlalchemy.orm import Session

import models
import schemas


def get_by_id(db: Session, magazine_id: int):
    return db.query(models.Magazine).filter(models.Magazine.id == magazine_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Magazine).offset(skip).limit(limit).all()


def create(db: Session, magazine: schemas.MagazineBase):
    db_magazine = models.Magazine(name=magazine.name)
    db.add(db_magazine)
    print("ff")
    db.commit()
    db.refresh(db_magazine)
    return db_magazine


def update(db: Session, magazine_id: int, magazine: schemas.MagazineBase):
    db_magazine = get_by_id(db, magazine_id)
    db_magazine.name = magazine.name
    db.commit()
    db.refresh(db_magazine)
    return db_magazine


def delete(db: Session, magazine_id: int):
    db_magazine = get_by_id(db, magazine_id)
    db.delete(db_magazine)
    db.commit()
