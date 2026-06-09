from psycopg2.extras import RealDictCursor

from app.database.connection import DatabaseConnection
from app.factories.review_factory import ReviewFactory
from app.repositories.user_repository import UserRepository


class ReviewRepository:
    def __init__(self):
        self.user_repository = UserRepository()


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

    def add_review(self, media_id, username, score, comment):
        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            user = self.user_repository.get_user_by_username(username)

            if user is None:
                return False

            cursor.execute(
"""
SELECT id
FROM review
WHERE media_id = %s
AND user_id = %s;
""", (media_id, user.id))

            existing_review = cursor.fetchone()

            if existing_review:
                cursor.execute(
"""
UPDATE review
SET score      = %s,
    comment    = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE id = %s;
""", (score, comment, existing_review["id"]))
            else:
                cursor.execute(
"""
INSERT INTO review (
    media_id,
    user_id,
    score,
    comment)
VALUES (%s, %s, %s, %s);
""", (media_id, user.id, score, comment))

            connection.commit()

            self.update_media_rating(media_id)

            return True

        except Exception as error:
            connection.rollback()
            print(error)
            return False

        finally:
            cursor.close()

    def update_review(self, review_id, username, score, comment):
        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            user = self.user_repository.get_user_by_username(username)

            if user is None:
                return False

            cursor.execute("""
                           SELECT media_id
                           FROM review
                           WHERE id = %s
                             AND user_id = %s;
                           """, (review_id, user.id))

            row = cursor.fetchone()

            if row is None:
                return False

            media_id = row["media_id"]

            cursor.execute("""
                           UPDATE review
                           SET score      = %s,
                               comment    = %s,
                               updated_at = CURRENT_TIMESTAMP
                           WHERE id = %s
                             AND user_id = %s;
                           """, (score, comment, review_id, user.id))

            connection.commit()

            self.update_media_rating(media_id)

            return cursor.rowcount > 0

        except Exception as error:
            connection.rollback()
            print(error)
            return False

        finally:
            cursor.close()

    def update_media_rating(self, media_id):

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute(
"""
UPDATE media
SET rating = sub.avg_rating
FROM (
    SELECT CAST(ROUND(AVG(score)) AS INTEGER) AS avg_rating
    FROM review
    WHERE media_id = %s
    ) AS sub
WHERE id = %s;
""", (media_id, media_id))

            connection.commit()

        finally:
            cursor.close()

    def user_has_reviewed_media(self, media_id, username):
        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            user = self.user_repository.get_user_by_username(username)

            if user is None:
                return False

            cursor.execute(
"""
SELECT id
FROM review
WHERE media_id = %s
AND user_id = %s;
""", (media_id, user.id))

            return cursor.fetchone() is not None

        finally:
            cursor.close()