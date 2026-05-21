from app.models.media import Media

class Book(Media):
    def __init__(self, id, title, release_year, description, rating, status_id,
                 author:str , publisher:str , page_count:int, isbn:str):
        super().__init__(id, title, release_year, description, rating, status_id)

        self._author = None
        self._publisher = None
        self._page_count = None
        self._isbn = None

        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.isbn = isbn

    """
    ==GET-SET==
    """
    @property
    def author(self) -> str:
        return self._author
    @author.setter
    def author(self, author) -> None:
        self._author = author

    @property
    def publisher(self) -> str:
        return self._publisher
    @publisher.setter
    def publisher(self, publisher) -> None:
        self._publisher = publisher

    @property
    def page_count(self) -> int:
        return self._page_count
    @page_count.setter
    def page_count(self, page_count) -> None:
        self._page_count = page_count

    @property
    def isbn(self) -> str:
        return self._isbn
    @isbn.setter
    def isbn(self, isbn) -> None:
        self._isbn = isbn


    """
    ==METHODS==
    """
    def get_type(self):
        return "Book"