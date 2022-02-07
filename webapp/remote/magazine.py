from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import schemas
from database import SessionLocal
from services import magazine_service

app = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/magazines/{magazine_id}", response_model=schemas.Magazine)
def read_magazine(magazine_id: int, db: Session = Depends(get_db)):
    db_magazine = magazine_service.get_by_id(db, magazine_id=magazine_id)
    if db_magazine is None:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return db_magazine


@app.get("/magazines")
def read_magazines(db: Session = Depends(get_db)):
    return magazine_service.get_all(db)


@app.post("/magazines", response_model=schemas.Magazine)
def create_magazine(magazine: schemas.MagazineBase, db: Session = Depends(get_db)):
    return magazine_service.create(db=db, magazine=magazine)


@app.put("/magazines/{magazine_id}", response_model=schemas.Magazine)
def update_magazine(magazine_id: int, magazine: schemas.MagazineBase, db: Session = Depends(get_db)):
    db_magazine = magazine_service.get_by_id(db, magazine_id=magazine_id)
    if db_magazine is None:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine_service.update(db=db, magazine_id=magazine_id, magazine=magazine)


@app.delete("/magazines/{magazine_id}", response_model=schemas.Magazine)
def delete_magazine(magazine_id: int, db: Session = Depends(get_db)):
    db_magazine = magazine_service.get_by_id(db, magazine_id=magazine_id)
    if db_magazine is None:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine_service.delete(db=db, magazine_id=magazine_id)
