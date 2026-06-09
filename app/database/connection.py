import os

import psycopg2
from dotenv import load_dotenv

"""
==SINGLETON==
"""
class DatabaseConnection:

    _connection = None

    @classmethod
    def get_connection(cls):
        load_dotenv()

        if cls._connection is None:

            cls._connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )

            print("Database connection created")

        return cls._connection

    @classmethod
    def close_connection(cls):

        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

            print("Database connection closed")