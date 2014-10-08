from ph_py.models.user import User


class UserDetails:

    def __init__(self, user_id, name, headline, created_at, username, image_url, profile_url, votes_count, posts_count,
                 maker_of_count, email, role, permissions, notifications, first_time_user):
        self.user = User(
            user_id,
            name,
            headline,
            created_at,
            username,
            image_url,
            profile_url
        )
        self.votes_count = votes_count
        self.posts_count = posts_count
        self.maker_of_count = maker_of_count
        self.email = email
        self.role = role
        self.permissions = permissions
        self.notifications = notifications
        self.first_time_user = first_time_user
