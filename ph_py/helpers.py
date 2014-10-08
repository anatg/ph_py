from .models.post import Post
from .models.vote import Vote
from .models.user import User
from .models.comment import Comment
from .models.related_link import RelatedLink
from .models.user_details import UserDetails
from .models.notification import Notification


def parse_notifications(notifications):
    return [
        Notification(
            notification["id"],
            notification["body"],
            notification["seen"],
            notification["sentence"],
            notification["type"],
            notification["reference"],
            notification["from_user"],
            notification["to_user"]
        ) for notification in notifications
    ]


def parse_details(details):
    return UserDetails(
        details["id"],
        details["name"],
        details["headline"],
        details["created_at"],
        details["username"],
        details["image_url"],
        details["profile_url"],
        details["votes_count"],
        details["posts_count"],
        details["maker_of_count"],
        details["email"],
        details["role"],
        details["permissions"],
        details["notifications"],
        details["first_time_user"]
    )


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
            posts["current_user"] if "current_user" in posts else None,
            posts["comments"],
            posts["votes"],
            posts["related_links"]
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
        return User(
            users["id"],
            users["name"],
            users["headline"],
            users["created_at"],
            users["username"],
            users["image_url"],
            users["profile_url"]
        )


def parse_votes(votes):
    if isinstance(votes, list):
        return [
            Vote(
                vote["id"],
                vote["created_at"],
                vote["post_id"],
                vote["user"]
            ) for vote in votes]
    elif votes:
        return Vote(
            votes["id"],
            votes["created_at"],
            votes["post_id"],
            votes["user"]
        )


def parse_related_links(related_links):
    if isinstance(related_links, list):
        return [
            RelatedLink(
                related_link["id"],
                related_link["url"],
                related_link["title"],
                related_link["domain"],
                related_link["favicon"],
                related_link["post_id"],
                related_link["user_id"],
            ) for related_link in related_links]
    elif related_links:
        return RelatedLink(
            related_links["id"],
            related_links["url"],
            related_links["title"],
            related_links["domain"],
            related_links["favicon"],
            related_links["post_id"],
            related_links["user_id"],
        )


def parse_comments(comments):
    if isinstance(comments, list):
        return [
            Comment(
                comment["id"],
                comment["body"],
                comment["created_at"],
                comment["post_id"],
                comment["parent_comment_id"],
                comment["user_id"],
                comment["child_comments_count"],
                comment["maker"],
                comment["user"],
                comment["child_comments"]
            ) for comment in comments]
    elif comments:
        return Comment(
            comments["id"],
            comments["body"],
            comments["created_at"],
            comments["post_id"],
            comments["parent_comment_id"],
            comments["user_id"],
            comments["child_comments_count"],
            comments["maker"],
            comments["user"],
            comments["child_comments"],
        )
