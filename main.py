from app.repositories.media_repository import MediaRepository
from app.database.connection import DatabaseConnection
from app.gui.main_window import MainWindow


#Turn the string blue
def blue(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;34m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string purple
def purple(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;35m{value}{value2}{value3}{value4}{value5}\033[0m"
#Separator
def sep():
    print(purple("+" * 40, "=" * 50, "+" * 40),sep='')



"==================TEST=================="
sep()


connection = DatabaseConnection.get_connection()
print("Connected successfully!")
connection.close()

sep()

repo = MediaRepository()
repo.test_connection()

sep()

books = repo.get_all_books()
for book in books:
    print(f"{book.title} by {book.author}")
    print(f"Status: {book.status_name}")
    print(f"Genres: {', '.join(book.genres)}")
    print(f"Sources: {', '.join(book.source_link)}")
    print(blue("-") * 40)

sep()

book = repo.get_book_by_id(1)

if book:
    print(f"{book.title} by {book.author} - {', '.join(book.genres)}")
else:
    print("Book not found")

sep()

app = MainWindow()
app.mainloop()