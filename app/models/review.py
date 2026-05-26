from datetime import datetime


class Review:
    def __init__(self, id, media_id, user_id, score, comment):
        self._id = id
        self._media_id = media_id
        self._user_id = user_id
        self._score = score
        self._comment = comment
        self._created_at = datetime.now()
        self._updated_at = None

    """
    ==GET-SET==
    """
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def media_id(self):
        return self._media_id
    @media_id.setter
    def media_id(self, media_id):
        self._media_id = media_id

    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        self._score = score

    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self, comment):
        self._comment = comment

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = datetime.now()