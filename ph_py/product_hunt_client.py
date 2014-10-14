import requests as r
from .helpers import parse_posts
from .helpers import parse_users
from .helpers import parse_votes
from .helpers import parse_details
from .helpers import parse_comments
from .error import ProductHuntError
from .helpers import parse_notifications
from .helpers import parse_related_links
from simplejson.scanner import JSONDecodeError


class ProductHuntClient:

    API_VERSION = 1
    API_BASE = "https://api.producthunt.com/v%d/" % API_VERSION
    ERROR_CODES = (401, 403, 404, 422)

    def __init__(self, client_id, client_secret, redirect_uri, dev_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        if dev_token:
            self.user_auth = {"access_token": dev_token}
        else:
            self.user_auth = None

        self.client_auth = self.oauth_client_token()

    def build_header(self, context):
        if context == "client":
            if self.client_auth is None:
                self.oauth_client_token()

            return {"Authorization": "Bearer %s" % self.client_auth["access_token"]}
        elif context == "user":
            if self.user_auth is None:
                raise ProductHuntError("No user authenticated!")

            return {"Authorization": "Bearer %s" % self.user_auth["access_token"]}

    def make_request(self, method, route, data, context="", retry=False):
        url = self.API_BASE + route

        headers = {}
        if context:
            headers = self.build_header(context)

        if method == "GET":
            response = r.get(url, headers=headers, data=data)
        elif method == "POST":
            response = r.post(url, headers=headers, data=data)
        elif method == "PUT":
            response = r.put(url, headers=headers, data=data)
        elif method == "DELETE":
            response = r.delete(url, headers=headers, params=data)

        try:
            json_data = response.json()
            if response.status_code in self.ERROR_CODES:
                if response.status_code == 401 and context == "client" and not retry:
                    self.oauth_client_token()
                    self.make_request(method, route, data, context, True)
                else:
                    raise ProductHuntError(json_data["error_description"], response.status_code)

            return json_data
        except JSONDecodeError:
            raise ProductHuntError("Error in parsing JSON from the Product Hunt API")

    def build_authorize_url(self):
        url = self.API_BASE + "oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code&scope=public private" % \
            (self.client_id, self.redirect_uri)

        return url

    # OAuth helpers
    def oauth_user_token(self, code):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
            "code": code
        }

        self.user_auth = self.make_request("POST", "oauth/token", data, "")
        return self.user_auth

    def oauth_client_token(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        self.client_auth = self.make_request("POST", "oauth/token", data, "")
        return self.client_auth

    # Post-related functions
    def get_todays_posts(self, context="client"):
        responses = self.make_request("GET", "posts", None, context)
        responses = responses["posts"]

        return parse_posts(responses)

    def get_previous_days_posts(self, days_ago, context="client"):
        responses = self.make_request("GET", "posts", {"days_ago": days_ago}, context)
        responses = responses["posts"]

        return parse_posts(responses)

    def get_specific_days_posts(self, day, context="client"):
        responses = self.make_request("GET", "posts", {"day": day}, context)
        responses = responses["posts"]

        return parse_posts(responses)

    def get_details_of_post(self, post_id, context="client"):
        post = self.make_request("GET", "posts/%d" % post_id, None, context)
        return parse_posts(post["post"])

    def create_a_post(self, url, name, tagline):
        data = {
            "post": {
                "url": url,
                "name": name,
                "tagline": tagline
            }
        }
        post = self.make_request("POST", "posts", data, "user")
        return parse_posts(post["post"])

    # Notification-related functions
    def show_notifications(self, older=None, newer=None, per_page=100, order=None):
        data = {
            "per_page": per_page
        }
        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        notifications = self.make_request("GET", "notifications", data, "user")
        return parse_notifications(notifications["notifications"])

    def clear_notifications(self):
        notifications = self.make_request("DELETE", "notifications", None, "user")
        return parse_notifications(notifications["notifications"])

    # User-related functions
    def get_users(self, older=None, newer=None, per_page=100, order=None, context="client"):
        data = {"per_page": per_page}

        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        users = self.make_request("GET", "users", data, context)
        return parse_users(users["users"])

    def get_user(self, username, context="client"):
        user = self.make_request("GET", "users/%s" % username, None, context)
        return parse_users(user["user"])

    # Vote-related functions
    def create_vote(self, post_id):
        vote = self.make_request("POST", "posts/%d/vote" % post_id, None, "user")
        return parse_votes(vote)

    def delete_vote(self, post_id):
        vote = self.make_request("DELETE", "posts/%d/vote" % post_id, None, "user")

        return parse_votes(vote)

    def get_user_votes(self, user_id, older=None, newer=None, per_page=100, order=None, context="client"):
        data = {"per_page": per_page}

        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        votes = self.make_request("GET", "users/%d/votes" % user_id, data, context)
        return parse_votes(votes["votes"])

    def get_post_votes(self, post_id, older=None, newer=None, per_page=100, order=None, context="client"):
        data = {"per_page": per_page}

        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        votes = self.make_request("GET", "posts/%d/votes" % post_id, data, context)
        return parse_votes(votes["votes"])

    # Comment-related functions
    def get_comments(self, post_id, older=None, newer=None, per_page=100, order=None, context="client"):
        data = {"per_page": per_page}

        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        comments = self.make_request("GET", "posts/%d/comments" % post_id, data, context)
        return parse_comments(comments["comments"])

    def create_comment(self, body, post_id, parent_comment_id=None):
        data = {
            "comment": {
                "body": body
            }
        }

        if parent_comment_id:
            data["comment"]["parent_comment_id"] = parent_comment_id

        comment = self.make_request("POST", "posts/%d/comments" % post_id, data, "user")
        return parse_comments(comment["comment"])

    def update_comment(self, body, comment_id):
        data = {
            "comment": {
                "body": body
            }
        }

        comment = self.make_request("PUT", "comments/%d" % comment_id, data, "user")
        return parse_comments(comment["comment"])

    # User Detail related functions
    def get_current_user_details(self):
        details = self.make_request("GET", "me", None, "user")
        return parse_details(details["user"])

    # Related-links functions
    def create_related_link(self, post_id, url, title=None):
        data = {"url": url}

        if title:
            data["title"] = title

        related_link = self.make_request("POST", "posts/%d/related_links" % post_id, data, "user")
        return parse_related_links(related_link)
    
    def update_related_link(self, post_id, related_link_id, title):
        data = {"title": title}

        related_link = self.make_request("PUT", "posts/%d/related_links/%d" % (post_id, related_link_id), data, "user")
        return parse_related_links(related_link)

    def delete_related_link(self, post_id, related_link_id):
        related_link = self.make_request("DELETE", "posts/%d/related_links/%d" % (post_id, related_link_id), None, "user")
        return parse_related_links(related_link)