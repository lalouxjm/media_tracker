from app.models.media import Media


class TVShow(Media):
    def __init__(self, id, title, release_year, description, rating, status_id,
                 creator:str, season_count:int, episode_count:int):
        super().__init__(id, title, release_year, description, rating, status_id)

        self._creator = None
        self._season_count = None
        self._episode_count = None

        self.creator = creator
        self.season_count = season_count
        self.episode_count = episode_count

    """
    ==GET-SET==
    """

    @property
    def creator(self) -> str:
        return self._creator
    @creator.setter
    def creator(self, creator) -> None :
        self._creator = creator

    @property
    def season_count(self) -> int:
        return self._season_count
    @season_count.setter
    def season_count(self, season_count:int) -> None :
        self._season_count = season_count

    @property
    def episode_count(self) -> int:
        return self._episode_count
    @episode_count.setter
    def episode_count(self, episode_count:int) -> None :
        self._episode_count = episode_count


    """
    ==METHODS==
    """
    def get_type(self):
        return "TV_SHOW"