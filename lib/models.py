from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Author(Base):
    # Authors: id:Integer,
    # name:String, 
    # books:list (relationship(Books))
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    books = relationship('Book', backref=backref('author'))

    def __repr__(self):
        return f'<#Author(id={self.id} name={self.name})>' 
    
class Book(Base):
    # id: Integer
	# book_name: String,
    # author_id:String (Foreign Key)
	# Publish_year: Integer
	# reviews: list (relationship(Reviews)
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    book_name = Column(String())
    publish_year = Column(Integer())
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    reviews = relationship('Review', backref=backref('book'))

    def __repr__(self):
        return f'<#Book(id={self.id} book_name={self.book_name} publish_year={self.publish_year} reviews={self.reviews})>,' 
    
class Review(Base):
    # id:Integer,
	# Comment: String
	# Name: string
	# Book_id:(Foreign Key)

    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    comment = Column(String())
    name = Column(String())
    book_id = Column(Integer, ForeignKey('books.id'))
    
    

    def __repr__(self):
        return f'<#Review(id={self.id} name={self.name} comment={self.comment})>,' 
            
           