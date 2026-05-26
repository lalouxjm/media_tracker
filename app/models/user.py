from datetime import datetime

class User:
    def __init__(self, username: str, password: str, email:str) -> None:
        self._username = None
        self._password = None
        self._email = None
        self._created_at = datetime.now()

        self.username = username
        self.password = password
        self.email = email



    """
    ==GET-SET==
    """

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username) -> None:
        self._username = username

    @property
    def password(self):
        return None
    @password.setter
    def password(self, password) -> None:
        self._password = password

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email) -> None:
        self._email = email

    @property
    def created_at(self):
        return self._created_at


