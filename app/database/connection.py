import psycopg2

class DatabaseConnection:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="media_tracker",
            user="postgres",
            password="postgrespwd"
        )