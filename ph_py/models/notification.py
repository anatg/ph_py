__author__ = 'ag'

from ph_py.models.user import User

class Notification:
    def __init__(self, notification_id, body, seen, sentence, type, reference, from_user, to_user, profile_url):
        self.notification_id = notification_id
        self.body = body
        self.seen = seen
        self.sentence = sentence
        self.type = type
        self.reference = reference
        self.from_user = User(
            from_user["id"],
            from_user["name"],
            from_user["headline"],
            from_user["created_at"],
            from_user["username"],
            from_user["image_url"]
        )
        self.to_user = User(
            to_user["id"],
            to_user["name"],
            to_user["headline"],
            to_user["created_at"],
            to_user["username"],
            to_user["image_url"]
        )
        self.profile_url = profile_url