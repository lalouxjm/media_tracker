


def purple(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;35m{value}{value2}{value3}{value4}{value5}\033[0m"
#Separator
def sep():
    print(purple("+" * 30), purple("=" * 50), purple("+" * 30),
          sep='')



"==================TEST=================="
sep()

from app.database.connection import DatabaseConnection
connection = DatabaseConnection.get_connection()
print("Connected successfully!")
connection.close()

sep()

from app.repositories.media_repository import MediaRepository
repo = MediaRepository()
books = repo.get_all_books()
for book in books:
    print(f"{book.title} by {book.author}")

sep()