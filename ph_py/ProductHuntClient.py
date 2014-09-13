import requests as r
from ph_py.models.post import Post
from ph_py.models.user import User


class ProductHuntClient:
    API_BASE = "https://api.producthunt.com/v1/"

    def __init__(self, client_id, client_secret, redirect_uri, dev_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        if dev_token:
            self.client_auth = {"access_token": dev_token}
        else:
            self.client_auth = None

        self.user_auth = None

    def build_header(self, context):
        if context == "client":
            if self.client_auth is None:
                raise Exception("No client authenticated!")

            return {"Authorization": "Bearer %s" % self.client_auth["access_token"]}
        elif context == "user":
            if self.user_auth is None:
                raise Exception("No user authenticated!")

            return {"Authorization": "Bearer %s" % self.user_auth["access_token"]}

    def make_request(self, method, route, data, context=""):
        url = self.API_BASE + route

        headers = {}
        if context:
            headers = self.build_header(context)

        if method == "GET":
            response = r.get(url, headers=headers, data=data)
        elif method == "POST":
            response = r.post(url, headers=headers, data=data)

        return response.json()

    def build_authorize_url(self):
        url = self.API_BASE + "oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code&scope=public private" % \
              (self.client_id, self.redirect_uri)

        return url

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

    def get_todays_posts(self, context="client"):
        responses = self.make_request("GET", "posts", None, context)
        responses = responses["posts"]

        return [
            Post(
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
            )
            for response in responses]

    def get_users(self, older=None, newer=None, per_page=100, order=None, context="client"):
        data = {
            "per_page": per_page
        }

        if older:
            data["older"] = older
        if newer:
            data["newer"] = newer
        if order:
            data["order"] = order

        users = self.make_request("GET", "users", data, context)
        users = users["users"]

        return [
            User(
                user["id"],
                user["name"],
                user["headline"],
                user["created_at"],
                user["username"],
                user["image_url"],
                user["profile_url"],
            )
            for user in users]

    def get_user(self, username, context="client"):
        user = self.make_request("GET", "users/%s" % username, None, context)
        user = user["user"]

        return User(
            user["id"],
            user["name"],
            user["headline"],
            user["created_at"],
            user["username"],
            user["image_url"],
            user["profile_url"],
        )


def main():
    client_id = "35587d189b3370c86629d4ba77027cfcaa6130970e4d3217da383042450ff501"
    client_secret = "42a385e7aae68c1ef243ae2634864ee7bc0576f66550f22149d510173c728cd8"
    redirect_uri = "http://localhost:5000"

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)
    phc.oauth_client_token()


if __name__ == "__main__":
    main()
