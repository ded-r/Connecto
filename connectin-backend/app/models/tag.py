"""
tag.py:
Хранит теги (Tag), которые могут использоваться в статьях (Article) или проектах (Project).
"""

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

# Проверяем, существует ли таблица, прежде чем объявлять её заново
article_tags_association = Table(
    "article_tags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
    extend_existing=True,  # Позволяет обновить таблицу, если она уже объявлена
)

project_tags_association = Table(
    "project_tags",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
    extend_existing=True,  # Аналогично, для таблицы project_tags
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Связи c Article
    articles = relationship(
        "Article",
        secondary=article_tags_association,
        back_populates="tags"
    )
    # Связи c Project
    projects = relationship(
        "Project",
        secondary=project_tags_association,
        back_populates="tags"
    )

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name}>"
