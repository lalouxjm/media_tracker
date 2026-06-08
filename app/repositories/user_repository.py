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

        cursor = connection.cursor

        try:
            cursor = connection.cursor(
                cursor_factory=RealDictCursor
            )

            cursor.execute(
"""
SELECT *
FROM app_user
WHERE username = %s
AND password = %s;
""", (username, password,))

            row = cursor.fetchone()

            if row is None:
                return None

            return UserFactory.create_user(row)

        finally:
            cursor.close()