from ph_py.models.post import Post
from ph_py.models.user import User


def parse_posts(posts):
    if isinstance(posts, list):
        return [
            Post(
                post["id"],
                post["name"],
                post["tagline"],
                post["created_at"],
                post["day"],
                post["comments_count"],
                post["votes_count"],
                post["discussion_url"],
                post["redirect_url"],
                post["screenshot_url"],
                post["maker_inside"],
                post["user"],
                post["current_user"] if "current_user" in post else None
            ) for post in posts]
    else:
        return Post(
            posts["id"],
            posts["name"],
            posts["tagline"],
            posts["created_at"],
            posts["day"],
            posts["comments_count"],
            posts["votes_count"],
            posts["discussion_url"],
            posts["redirect_url"],
            posts["screenshot_url"],
            posts["maker_inside"],
            posts["user"],
            posts["current_user"] if "current_user" in posts else None
        )


def parse_users(users):
    if isinstance(users, list):
        return [
            User(
                user["id"],
                user["name"],
                user["headline"],
                user["created_at"],
                user["username"],
                user["image_url"],
                user["profile_url"]
            ) for user in users]
    else:
        User(
            users["id"],
            users["name"],
            users["headline"],
            users["created_at"],
            users["username"],
            users["image_url"],
            users["profile_url"]
        )
