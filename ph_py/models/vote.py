class Vote:

    def __init__(self, vote_id, created_at, post_id, user):
        from .. import helpers

        self.vote_id = vote_id
        self.created_at = created_at
        self.post_id = post_id
        self.user = helpers.parse_users(user)
