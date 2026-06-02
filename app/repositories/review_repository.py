from psycopg2.extras import RealDictCursor

from app.database.connection import DatabaseConnection
from app.factories.review_factory import ReviewFactory


class ReviewRepository:

    def get_reviews_by_media_id(self, media_id):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute("""
SELECT
r.id,
r.media_id,
r.user_id,
u.username,
r.score,
r.comment,
r.created_at,
r.updated_at
FROM review r
JOIN app_user u
ON r.user_id = u.id
WHERE r.media_id = %s
ORDER BY r.created_at ASC;
""", (media_id,))

            rows = cursor.fetchall()

            return [
                ReviewFactory.create_review(row)
                for row in rows
            ]

        finally:
            cursor.close()