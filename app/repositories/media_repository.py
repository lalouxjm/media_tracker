from psycopg2.extras import RealDictCursor
from app.database.connection import DatabaseConnection
from app.factories.media_factory import MediaFactory


class MediaRepository:

    connection = DatabaseConnection.get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    "============================================================================="
    "BOOKS"
    "============================================================================="

    def add_books(self, media):
        pass

    def get_all_books(self):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(
                cursor_factory=RealDictCursor
            )

            cursor.execute("""
SELECT m.id,
m.title,
m.release_year,
m.description,
m.rating,
s.id AS status_id,
s.name AS status_name,
b.author,
b.publisher,
b.page_count,
b.isbn,
STRING_AGG(DISTINCT g.name, ', ') AS genres,
STRING_AGG(DISTINCT sl.platform_name || ' (' || sl.availability_type || ')', ', ') AS source_links,
'BOOK' AS media_type
FROM media AS m
JOIN book AS b
ON m.id = b.media_id
JOIN status AS s
ON m.status_id = s.id

LEFT JOIN media_genre AS mg
ON m.id = mg.media_id
LEFT JOIN genre AS g
ON mg.genre_id = g.id
LEFT JOIN source_link AS sl
ON m.id = sl.media_id
GROUP BY m.id, s.id, b.media_id
ORDER BY m.title;
""")

            rows = cursor.fetchall()
            books = []

            for row in rows:
                books.append(
                    MediaFactory.create_media(row)
                )

            return books

        finally:
            cursor.close()
            connection.close()

    def get_book_by_id(self, media_id):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            query = """
SELECT m.id, 
m.title, 
m.release_year, 
m.description, 
m.rating, 
s.id AS status_id, 
s.name AS status_name, 
m.created_at, 
m.updated_at, 
b.author, b.publisher, 
b.page_count, b.isbn, 
STRING_AGG(DISTINCT g.name, ', ') AS genres, \
STRING_AGG(DISTINCT sl.platform_name || ' (' || sl.availability_type || ')', ', ' ) AS source_links, 
'BOOK' AS media_type

FROM media m
JOIN book b ON m.id = b.media_id
JOIN status s ON m.status_id = s.id
LEFT JOIN media_genre mg ON m.id = mg.media_id
LEFT JOIN genre g ON mg.genre_id = g.id
LEFT JOIN source_link sl ON m.id = sl.media_id
WHERE m.id = %s
GROUP BY m.id, s.id, b.media_id 
"""
            cursor.execute(query, (media_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return MediaFactory.create_media(row)

        finally:
            cursor.close()
            connection.close()

    def update_book(self, media):
        pass
    def delete_delete(self, media_id):
        pass

    "============================================================================="
    "MOVIES"
    "============================================================================="

    def get_all_movies(self):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute("""
SELECT m.id,
m.title,
m.release_year,
m.description,
m.rating,
s.id AS status_id,
s.name AS status_name,
mo.director,
mo.duration_minutes,
STRING_AGG(DISTINCT g.name, ', ') AS genres,
STRING_AGG(DISTINCT sl.platform_name || ' (' || sl.availability_type || ')', ', ') AS source_links,
'MOVIE' AS media_type
FROM media AS m
JOIN movie AS mo
ON m.id = mo.media_id
JOIN status AS s
ON m.status_id = s.id
LEFT JOIN media_genre AS mg
ON m.id = mg.media_id
LEFT JOIN genre AS g
ON mg.genre_id = g.id
LEFT JOIN source_link AS sl
ON m.id = sl.media_id
GROUP BY m.id, s.id, mo.media_id
ORDER BY m.title;
""")

            rows = cursor.fetchall()
            movies = []

            for row in rows:
                movies.append(MediaFactory.create_media(row))

            return movies

        finally:
            cursor.close()
            connection.close()

    "============================================================================="
    "TV SHOWS"
    "============================================================================="

    def get_all_tv_shows(self):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute("""
SELECT m.id,
m.title,
m.release_year,
m.description,
m.rating,
s.id AS status_id,
s.name AS status_name,
tv.creator,
tv.season_count,
tv.episode_count,
STRING_AGG(DISTINCT g.name, ', ') AS genres,
STRING_AGG(DISTINCT sl.platform_name || ' (' || sl.availability_type || ')', ', ') AS source_links,
'TV_SHOW' AS media_type
FROM media AS m
JOIN tv_show AS tv
ON m.id = tv.media_id
JOIN status AS s
ON m.status_id = s.id
LEFT JOIN media_genre AS mg
ON m.id = mg.media_id
LEFT JOIN genre AS g
ON mg.genre_id = g.id
LEFT JOIN source_link AS sl
ON m.id = sl.media_id
GROUP BY m.id, s.id, tv.media_id
ORDER BY m.title;
""")

            rows = cursor.fetchall()
            tvshows = []

            for row in rows:
                tvshows.append(MediaFactory.create_media(row))

            return tvshows

        finally:
            cursor.close()
            connection.close()

    def test_connection(self):

        connection = DatabaseConnection.get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute("SELECT * FROM status")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        connection.close()
