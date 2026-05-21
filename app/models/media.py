from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, id:int, title:str, release_year:int, description:str, rating: float, status_id: int):

        self._id = None
        self._title = None
        self._release_year = None
        self._description = None
        self._rating = None
        self._status_id = None

        self.id = id
        self.title = title
        self.release_year = release_year
        self.description = description
        self.rating = rating
        self.status_id = status_id

    """
    ==GET-SET==
    """
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def release_year(self) -> int:
        return self._release_year
    @release_year.setter
    def release_year(self, value: int) -> None:
        self._release_year = value

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def rating(self) -> float:
        return self._rating
    @rating.setter
    def rating(self, value: float) -> None:
        self._rating = value

    @property
    def status_id(self) -> int:
        return self._status_id
    @status_id.setter
    def status_id(self, value: int) -> None:
        self._status_id = value



    """
    ==ABSTRACT METHODS==
    """
    @abstractmethod
    def get_type(self):
        ...