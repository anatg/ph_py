__author__ = 'ag'

from ph_py.models.post import Post
from ph_py.models.notification import Notification

def create_post(responses):
    response = [Post(
        response["id"],
        response["name"],
        response["tagline"],
        response["created_at"],
        response["day"],
        response["comments_count"],
        response["votes_count"],
        response["discussion_url"],
        response["redirect_url"],
        response["screenshot_url"],
        response["maker_inside"],
        response["user"],
        response["current_user"] if "current_user" in response else None
    ) for response in responses
    ]
    return response

