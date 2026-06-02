import psycopg2

"""
==SINGLETON==
"""
class DatabaseConnection:

    _connection = None

    @classmethod
    def get_connection(cls):

        if cls._connection is None:

            cls._connection = psycopg2.connect(
                host="localhost",
                database="media_tracker",
                user="postgres",
                password="postgrespwd"
            )

            print("Database connection created")

        return cls._connection

    @classmethod
    def close_connection(cls):

        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

            print("Database connection closed")