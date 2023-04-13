#!/usr/bin/env python3

from models import Author, Book, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self):
        self.authors = [author for author in session.query(Author)]
        #bring in other models
        self.start()
    
    def start(self):
        print("Welcome to our Book App")
        print("Please give us your name!")
        f_name = input("First name?")
        print("Thanks!")
        #get last name
        for idx, auth in enumerate(self.authors):    
            print(f'{idx+1}. {auth.name}')
        #welcome statement
        choice = input("what do you want to do?")
        #three choices, see all authors, see all books, add an author
        
        if choice == 1:
            print("Goodbye!")


if __name__ == "__main__":
    engine = create_engine('sqlite:///lib/models.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()
