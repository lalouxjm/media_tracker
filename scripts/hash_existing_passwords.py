import bcrypt
from app.database.connection import DatabaseConnection

connection = DatabaseConnection.get_connection()
cursor = connection.cursor()

cursor.execute('''SELECT id, password FROM app_user''')
users = cursor.fetchall()

for user_id, plain_password in users:
    if plain_password.startswith("$2b$"):
        continue

    hashed_password = bcrypt.hashpw(
        plain_password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    cursor.execute(
"""
UPDATE app_user
SET password = %s
WHERE id = %s;
""", (hashed_password, user_id))

connection.commit()

cursor.close()
DatabaseConnection.close_connection()

print("Passwords hashed successfully")