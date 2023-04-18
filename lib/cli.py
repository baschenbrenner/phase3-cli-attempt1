#!/usr/bin/env python3

from models import Author, Book, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import ipdb


class CLI:

    def __init__(self):
        self.authors = [author for author in session.query(Author)]
        self.books = [book for book in session.query(Book)]
        # bring in other models
        self.name = self.get_name()
        self.start()

    # Was going to make a dict mapped to choices, but seems like we would still need an if
    # statement so maybe an unneeded abstraction
    # def options_dict(self):
    #     return {
    #         'pa': self.print_indexed_items(self.authors, 'name'),
    #     }

    def get_name(self):
        print("Welcome to our Book App")
        print("Please give us your name!")
        f_name = input("First name?")
        print("Thanks!")
        return f_name

    def start(self):

        # self.print_indexed_items(self.authors, 'name')
        choice = ''
        while (not CLI.valid_choice(['pa', 'pb', 'aa', 'exit'], choice)):
            choice = input(
                "To see all authors enter 'pa'\nTo see all books enter 'pb'\nTo add an author type 'aa'\nTo exit type 'exit'\n")

        while choice != 'exit':
            if choice == 'pa':
                self.print_indexed_items(self.authors, 'name')
                choice = self.list_author_options()
            elif choice == 'pb':
                self.print_indexed_items(self.books, 'book_name')
            elif choice == 'menu':
                self.start()
            elif choice == 'aa':
                author_name = self.get_author_name()
                Author.create_and_add_to_cli(author_name, self)
                self.start()

        print('Have a nice day!')
        quit()

        # three choices, see all authors, see all books, add an author

    def print_indexed_items(self, items, attr):
        [print(f'{idx + 1}. {getattr(item, attr)}')
         for idx, item in enumerate(items)]

    def list_author_options(self):

        self.print_indexed_items(self.authors, 'name')
        choice = ''

        while (not CLI.valid_choice(['pa', 'menu', 'exit'], choice) and not choice.isdigit()):
            choice = input(
                "To see all books by an author enter the number of the author\nTo return to main menu type 'menu'\nTo exit type 'exit'\n")

        if choice.isdigit() and int(choice) - 1 in range(len(self.authors)):
            author = self.authors[int(choice) - 1]
            self.print_indexed_items(author.books, 'book_name')
        elif choice.isdigit():
            self.list_author_options()
        elif choice == 'pa':
            self.print_indexed_items(self.authors, 'name')
            self.list_author_options()

        return choice

    @ classmethod
    def valid_choice(self, options, input):
        return input in options

    def get_author_name(self):
        return input('Please enter name of author: ')


if __name__ == "__main__":
    engine = create_engine('sqlite:///lib/models.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()
