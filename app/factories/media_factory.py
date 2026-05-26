from app.models.books import Book
from app.models.movie import Movie
from app.models.tv_show import TVShow


class MediaFactory:

    @staticmethod
    def create_media(data):
        media_type = data['media_type']

        if media_type == "BOOK":
            return Book(...)

        elif media_type == "MOVIE":
            return Movie(...)

        elif media_type == "TV_SHOW":
            return TVShow(...)

        else:
            raise Exception("Media type not supported")