class Genre:
    def __init__(self, id: int, name: str) -> None:
        self._id = None
        self._name = None

        self.id = id
        self.name = name

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value


    def __str__(self):
        return self.name