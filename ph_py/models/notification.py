class Notification:

    def __init__(self, notification_id, body, seen, sentence, type, reference, from_user, to_user):
        from .. import helpers

        self.notification_id = notification_id
        self.body = body
        self.seen = seen
        self.sentence = sentence
        self.type = type
        self.reference = reference
        self.from_user = helpers.parse_users(from_user)
        self.to_user = helpers.parse_users(to_user)
