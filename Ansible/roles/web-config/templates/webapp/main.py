import os

from fastapi import FastAPI
from sqlalchemy.sql import text

import models
from database import engine
from remote import article, article_type, author, magazine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(article.app)
app.include_router(article_type.app)
app.include_router(author.app)
app.include_router(magazine.app)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if os.path.isfile("/var/www/app/drop.sql"):
    with engine.connect() as con:
        file = open("/var/www/app/drop.sql")
        query = text(file.read())
        con.execute(query)
        os.remove("/var/www/app/drop.sql")