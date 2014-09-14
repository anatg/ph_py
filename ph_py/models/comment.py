__author__ = 'ag'

from ph_py.models.user import User


class Comment:
    def __init__(self, comment_id, body, created_at, post_id, parent_comment_id, user_id,
                 child_comments_count, maker, user, child_comments=None):
        self.id = comment_id
        self.body = body
        self.created_at = created_at
        self.post_id = post_id
        self.parent_comment_id = parent_comment_id
        self.user_id = user_id
        self.child_comments_count = child_comments_count
        self.maker = maker
        self.user = User(
            user["id"],
            user["name"],
            user["headline"],
            user["created_at"],
            user["username"],
            user["image_url"],
            user["profile_url"]
        )
        self.child_comments = self.build_comment_tree(child_comments)


    @staticmethod
    def build_comment_tree(children):
        child_objects = []

        for child in children:
            to_insert = Comment(
                child["id"],
                child["body"],
                child["created_at"],
                child["post_id"],
                child["parent_comment_id"],
                child["user_id"],
                child["child_comments_count"],
                child["maker"],
                child["user"],
                child["child_comments"],
            )
            child_objects.append(to_insert)

        return child_objects