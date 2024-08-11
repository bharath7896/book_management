from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class Book(Base):
  __tablename__ = "books"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  genre = Column(String)
  year_published = Column(Integer)
  summary = Column(Text)
  reviews = relationship("Review", back_populates="book")


