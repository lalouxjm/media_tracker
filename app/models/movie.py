from app.models.media import Media


class Movie(Media):
    def __init__(self, id, title, release_year, description, rating, status_id,
                 director: str, duration_minutes:int):
        super().__init__(id, title, release_year, description, rating, status_id)
        self._director = None
        self._duration_minutes = None

        self.director = director
        self.duration_minutes = duration_minutes

    """
    ==GET-SET==
    """
    @property
    def director(self) -> str:
        return self._director
    @director.setter
    def director(self, director) -> None:
        self._director = director

    @property
    def duration_minutes(self) -> int:
        return self._duration_minutes
    @duration_minutes.setter
    def duration_minutes(self, duration_minutes) -> None:
        self._duration_minutes = duration_minutes


    """
    ==METHODS
    """

    def get_type(self):
        return "Movie"