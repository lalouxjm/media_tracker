from app.models.user import User

class UserFactory:

    @staticmethod
    def create_user(data) -> User:

        user = User(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )

        user._id = data['id']

        return user