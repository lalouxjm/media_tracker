class SourceLink:
    def __init__(self, id: int, media_id: int, platform_name: str, url: str, availability_type: str ) -> None:
        self._id = None
        self._media_id = None
        self._platform_name = None
        self._url = None
        self._availability_type = None

        self.id = id
        self.media_id = media_id
        self.platform_name = platform_name
        self.url = url
        self.availability_type = availability_type

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def media_id(self) -> int:
        return self._media_id
    @media_id.setter
    def media_id(self, value: int) -> None:
        self._media_id = value

    @property
    def platform_name(self) -> str:
        return self._platform_name
    @platform_name.setter
    def platform_name(self, value: str) -> None:
        self._platform_name = value

    @property
    def url(self) -> str:
        return self._url
    @url.setter
    def url(self, value: str) -> None:
        self._url = value

    @property
    def availability_type(self) -> str:
        return self._availability_type
    @availability_type.setter
    def availability_type(self, value: str) -> None:
        self._availability_type = value


