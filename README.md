Starting out
Test test
We propose an Author-Books-Reviews CLI for our phase 3 project

We are going to work collaboratively on the project with intermittent meetings to touch base on parts of the project

### Creating tables/models
 - cd Project_folder
 - create lib folder
 - run `alembic init migrations`
 - touch models.py
 - ls migrations/env.py. Change en.py line 21
	- from models import Base
	- target_metadata = Base.metadata
 - ls alembic.ini, point to correct database
	- sqlalchemy.url = sqlite:///models.db
 - Create Base class and other table classes in models.py
 - run `alembic revision --autogenerate -m 'Adding classes'`
 - `alembic upgrade head`


Tables
Authors: id:Integer,
   name:String, 
               books:list (relationship(Books))


Books: id: Integer
	book_name: String,
    author_id:String (Foreign Key)
	Publish_year: Integer
	reviews: list (relationship(Reviews)


Reviews: id:Integer,
	    Comment: String
	 Name: string
	   Book_id:(Foreign Key)
	




Where the 

CLI Functionality
App starts and gives a list of authors that the user can choose from
User selects an author
Display a list of books that belong to chosen author
Give the user an option to add a new book or select a specific book to view more details about
If user selects create new book, prompts to get data about the book
Else if user selects a specific book , display reviews for book with option to create review




Add to any table 
Starting menu:
See all authors, add an author, add a book and author, see all books, 

Build seeds data for 10 Authors, 3-5 books each and 0-3 reviews per book
Then test out with other instructors to add information


Models - models.py - Aastha
Work on bringing the seed data in through an API - Dustin
Writing CLI functionality plan 
Working on cli.py file 


Welcome to our Book App!
Please give us your name:
First Name?
Last Name?
Menu Display
1. Author List
2. Show my Name
3. Exit
What you would like to do?

