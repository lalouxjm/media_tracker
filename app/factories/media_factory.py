from app.models.books import Book
from app.models.movie import Movie
from app.models.tv_show import TVShow


class MediaFactory:

    @staticmethod
    def create_media(data):
        media_type = data['media_type']

        if data["media_type"] == "BOOK":
            return Book(
                id=data["id"],
                title=data["title"],
                release_year=data["release_year"],
                description=data["description"],
                rating=data["rating"],
                status_id=data["status_id"],

                author=data["author"],
                publisher=data["publisher"],
                page_count=data["page_count"],
                isbn=data["isbn"],

                status_name=data.get("status_name"),
                genres=data["genres"].split(", ") if data.get("genres") else [],
                source_links=data["source_links"].split(", ") if data.get(
                    "source_links") else []
            )

        elif media_type == "MOVIE":
            return Movie(
                media_id=data["media_id"],
                title=data["title"],
                release_year=data["release_year"],
                description=data["description"],
                rating=data["rating"],
                status_id=data["status_id"],
                director=data["director"],
                duration_minutes=data["duration_minutes"]
            )

        elif media_type == "TV_SHOW":
            return TVShow(
                media_id=data["media_id"],
                title=data["title"],
                release_year=data["release_year"],
                description=data["description"],
                rating=data["rating"],
                status_id=data["status_id"],
                creator=data["creator"],
                season_count=data["season_count"],
                episode_count=data["episode_count"]
            )

        else:
            raise ValueError(f"Unknown media type: {media_type}")