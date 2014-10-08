class Post:

    def __init__(self, post_id, name, tagline, created_at, day, comments_count, votes_count, discussion_url,
                 redirect_url, screenshot_url, maker_inside, user, current_user, comments=None, votes=None,
                 related_links=None):
        from .. import helpers

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
        self.user = helpers.parse_users(user)
        self.comments = helpers.parse_comments(comments)
        self.votes = helpers.parse_votes(votes)
        self.related_links = helpers.parse_related_links(related_links)
