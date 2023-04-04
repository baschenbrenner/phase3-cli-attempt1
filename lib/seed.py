import random as rc


from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book, Review

if __name__ == '__main__':

   engine = create_engine('sqlite:///models.db')
   Session = sessionmaker(bind=engine)
   session = Session()


   session.query(Author).delete()
   session.query(Book).delete()
   session.query(Review).delete()
   session.commit()

faker = Faker()
def create_author_objects(n, faker):
   authors = []
   for i in range(n):
       auth = Author(
           name=faker.name(),
       )
       session.add(auth)
       session.commit()
       authors.append(auth)
       
   return authors



for a in create_author_objects(20, faker):
   print(a)

def create_book_objects(n, faker):
   books = []
   number_of_authors=session.query(Author).count()
   all_authors = session.query(Author).all

   for i in range(n):
       


       nouns = ["apple", "car", "dog", "house", "chair", "phone", "tree", "book", "cat", "table","desk", "computer", "flower", "bike", "mountain", "river", "ocean", "television", "camera","guitar", "pen", "pencil", "notebook", "bag", "shoe", "shirt", "pants", "dress", "hat","jacket", "sun", "moon", "star", "cloud", "rain", "snow", "ice", "fire", "earth", "sky","beach", "lake", "island", "jungle", "forest", "bird", "fish", "insect", "plane", "train","bus", "ship", "rocket", "keyboard", "mouse", "speaker", "microphone", "flowerpot", "globe","map", "clock", "chair", "tablecloth", "plate", "fork", "knife", "spoon", "candle", "painting","sculpture", "statue", "camera", "film", "picture", "photograph", "mirror", "towel", "soap","shampoo", "conditioner", "toothbrush", "toothpaste", "pillow", "blanket", "sheet", "mattress","window", "door", "ladder", "mirror", "laptop", "desktop", "printer", "scanner"]
       verbs = ["run", "walk", "jump", "swim", "climb", "drive", "ride", "fly", "read", "write", "speak", "listen", "sing", "dance", "draw", "paint", "cook", "eat", "drink", "sleep", "wake", "dream", "think", "ponder", "meditate", "breathe", "laugh", "cry", "smile", "frown", "nod", "wave", "point", "touch", "hold", "grasp", "push", "pull", "lift", "carry", "throw", "catch", "kick", "punch", "fight", "shoot", "aim", "hit", "miss", "kill", "die", "live", "survive", "thrive", "create", "build", "make", "design", "invent", "discover", "learn", "study", "teach", "train", "mentor", "lead", "follow", "guide", "help", "assist", "support", "encourage", "motivate", "inspire", "imagine", "visualize", "plan", "organize", "execute", "implement", "evaluate", "assess", "test", "measure", "analyze", "interpret", "conclude", "decide", "choose", "select", "pick", "vote", "win", "lose", "succeed", "fail", "try"]
       adverbs = ["quickly", "slowly", "quietly", "loudly", "softly", "rudely", "politely", "kindly", "cruelly", "gently","harshly", "happily", "sadly", "angrily", "anxiously", "eagerly", "calmly", "bravely", "cowardly", "boldly","timidly", "shyly", "confidently", "carefully", "carelessly", "efficiently", "effectively", "ineffectively", "honestly","dishonestly", "generously", "selfishly", "gracefully", "clumsily", "awkwardly", "smoothly", "roughly", "politically","financially", "economically", "morally", "ethically", "legally", "intentionally", "accidentally", "miraculously", "completely","partially", "mostly", "rarely", "often", "seldom", "always", "never", "maybe", "perhaps", "possibly", "certainly","definitely", "absolutely", "positively", "naturally", "artificially", "originally", "simply", "complexly", "seriously","humorously", "solemnly", "indifferently", "passionately", "urgently", "casually", "honestly", "faithfully", "hopefully","optimistically", "pessimistically", "realistically", "fantastically", "literally", "figuratively", "verbally", "nonverbally", "precisely","vaguely", "directly", "indirectly", "temporarily", "permanently", "mentally", "physically", "emotionally", "spiritually", "culturally"]
       book_titles = ["The Whispering Sun", "The Glass Forest", "The Savage Tide", "The Lost Heirloom", "The Misty Mountains", "The Timekeeper's Daughter", "The Enchanted Garden", "The Secret of the Seventh Star", "The Broken Mirror", "The Cursed Locket", "The Island of the Forgotten", "The Forbidden Door", "The Midnight Caller", "The Ghostly Manor", "The Crimson Key", "The Shimmering Sands", "The Silver Serpent", "The Haunted Tower", "The Ancient Book", "The Blackwood Legacy", "The Hidden City", "The Crystal Lake", "The Golden Hourglass", "The Emerald Eye", "The Spellbound Amulet", "The Whispering Wind", "The Rusty Key", "The Clockmaker's Daughter", "The Moonlit Garden", "The Enchanted Mirror", "The Mysterious Island", "The Lost Relic", "The Vanishing Village", "The Forbidden Scroll", "The Shrouded Forest", "The Twisted Tree", "The Shadowed Path", "The Tangled Web", "The Diamond Thief", "The Crimson Rose", "The Whispering Woods", "The Forgotten Kingdom", "The Hidden Garden", "The Secret Society", "The Silent Forest", "The Dark Labyrinth", "The Enchanted Kingdom", "The Cursed Heir", "The Haunted Manor", "The Phantom's Curse", "The Secret of the Black Pearl", "The Vanished Crown", "The Burning Sands", "The Crystal Skull", "The Timeless Treasure", "The Eternal Flame", "The Lost City of Gold", "The Cursed Talisman", "The Shattered Mirror", "The Shadowed Tower", "The Wandering Ghost", "The Midnight Train", "The Haunting of Hillside Manor", "The Enchanted Forest", "The Secret of the White Rose", "The Crystal Maze", "The Mystic's Apprentice", "The Chosen One", "The Ghostly Guardian", "The Sapphire Scarab", "The Hidden Scroll", "The Fallen Star", "The Cursed Castle", "The Diamond Dagger", "The Enchanted River", "The Lost Oasis", "The Secret of the Black Stone", "The Vanished Heir", "The Burning Scroll", "The Forgotten Forest", "The Phantom's Lair", "The Haunted Inn", "The Secret of the Crystal Cave", "The Shadowed Forest", "The Wandering Witch", "The Midnight Curse", "The Enchanted Garden Gate", "The Secret of the Silent Sands", "The Crystal Key", "The Mystic's Quest", "The Chosen Few", "The Ghostly Whisper", "The Sapphire Secret", "The Hidden Tomb"]

       if i<5:
          
           book = Book(
                book_name=f'The {nouns[rc.randint(0,94)]} {adverbs[rc.randint(0,94)]} {verbs[rc.randint(0,94)]}s like {nouns[rc.randint(0,94)]}',
                publish_year=faker.year(),
                author_id= rc.randint(1,number_of_authors)
            )
       else:
          book = Book(
                book_name=book_titles[i],
                publish_year=faker.year(),
                author_id= rc.randint(1,number_of_authors)
            )
          
       books.append(book)

       
   session.add_all(books)
   session.commit()    
   return books

for b in create_book_objects(60, faker):
   print(b)

def create_review_objects(n, faker):
   reviews = []
   book_list = session.query(Book).all()
   for i in range(n):
       rev = Review(
           comment=faker.sentence(),
           name=faker.name(),
           book_id= rc.choice(book_list).id
       )

       reviews.append(rev)

   session.add_all(reviews)
   session.commit()    
       
   return reviews

for r in create_review_objects(100, faker):
   print(r)



