from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Review(Base):
  __tablename__ = "reviews"
  id = Column(Integer, primary_key=True, index=True)
  book_id = Column(Integer, ForeignKey("books.id"))
  user_id = Column(Integer)  # Assuming you have a users table
  review_text = Column(Text)
  rating = Column(Integer)
  book = relationship("Book", back_populates="reviews")
