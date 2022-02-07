from pydantic import BaseModel


class MagazineBase(BaseModel):
    name: str


class Magazine(MagazineBase):
    id: int

    class Config:
        orm_mode = True


class ArticleTypeBase(BaseModel):
    type: str


class ArticleType(ArticleTypeBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    author: str


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    magazine_id: int
    article_type_id: int
    author_id: int


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
