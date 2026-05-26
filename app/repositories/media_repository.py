from psycopg2.extras import RealDictCursor
from app.database.connection import DatabaseConnection
from app.factories.media_factory import MediaFactory


class MediaRepository:

    connection = DatabaseConnection.get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    def add_media(self, media):
        pass
    def get_all_media(self):
        pass

    def get_all_books(self):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
SELECT
m.id,
m.title,
m.release_year,
m.description,
m.rating,
m.status_id,
b.author,
b.publisher,
b.page_count,
b.isbn,
'BOOK' AS media_type
FROM media AS m
JOIN book AS b ON m.id = b.media_id;
        """)

        rows = cursor.fetchall()

        books = []

        for row in rows:
            books.append(
                MediaFactory.create_media(row)
            )

        return books

    def get_media_by_id(self, media_id):
        pass
    def update_media(self, media):
        pass
    def delete_media(self, media_id):
        pass

