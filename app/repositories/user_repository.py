import bcrypt
from psycopg2.extras import RealDictCursor

from app.database.connection import DatabaseConnection
from app.factories.user_factory import UserFactory


class UserRepository:
    def get_user_by_username(self, username):
        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(
                cursor_factory=RealDictCursor
            )
            cursor.execute(
"""
SELECT *
FROM app_user
WHERE username = %s;
""", (username,))

            row = cursor.fetchone()

            if row is None:
                return None

            return UserFactory.create_user(row)

        finally:
            cursor.close()


    def verify_login(self, username, password):
        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute(
"""
SELECT *
FROM app_user
WHERE username = %s;
""", (username,))

            row = cursor.fetchone()

            if row is None:
                return None

            stored_password = row["password"]

            password_is_valid = bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password.encode("utf-8")
            )

            if not password_is_valid:
                return None

            return UserFactory.create_user(row)

        finally:
            cursor.close()