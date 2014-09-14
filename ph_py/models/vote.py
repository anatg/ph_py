from ph_py.models.user import User


class Vote:
    def __init__(self, vote_id, created_at, post_id, user):
        self.vote_id = vote_id
        self.created_at = created_at
        self.post_id = post_id
        self.user = User(
            user["id"],
            user["name"],
            user["headline"],
            user["created_at"],
            user["username"],
            user["image_url"],
            user["profile_url"]
        )
