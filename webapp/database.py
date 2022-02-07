from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://ugly:betty@localhost:15432/magazine"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()