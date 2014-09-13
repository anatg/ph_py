__author__ = 'ag'

from ph_py.models.user import User


class Post:
    def __init__(self, post_id, name, tagline, created_at, day, comments_count, votes_count, discussion_url,
                 redirect_url, screenshot_url, maker_inside, user, current_user=None):
        self.id = post_id
        self.name = name
        self.tagline = tagline
        self.created_at = created_at
        self.day = day
        self.comments_count = comments_count
        self.votes_count = votes_count
        self.discussion_url = discussion_url
        self.redirect_url = redirect_url
        self.screenshot_url = screenshot_url
        self.maker_inside = maker_inside
        self.current_user = current_user
        self.user = User(
            user["id"],
            user["name"],
            user["headline"],
            user["created_at"],
            user["username"],
            user["image_url"],
            user["profile_url"]
        )
