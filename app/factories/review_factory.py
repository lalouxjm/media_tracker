from app.models.review import Review


class ReviewFactory:

    @staticmethod
    def create_review(data):
        return Review(
            id=data["id"],
            media_id=data["media_id"],
            user_id=data["user_id"],
            username=data["username"],
            score=data["score"],
            comment=data["comment"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )