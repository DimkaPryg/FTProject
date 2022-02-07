from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base


class Magazine(Base):
    __tablename__ = "magazines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class ArticleTypes(Base):
    __tablename__ = "article_types"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    magazine_id = Column(Integer, ForeignKey("magazines.id"))
    article_type_id = Column(Integer, ForeignKey("article_types.id"))
    author_id = Column(Integer, ForeignKey("author.id"))
