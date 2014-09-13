import helpers
import requests as r


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

        return helpers.parse_posts(responses)

    def get_previous_days_posts(self, days_ago, context="client"):
        responses = self.make_request("GET", "posts", {"days_ago": days_ago}, context)
        responses = responses["posts"]

        return helpers.parse_posts(responses)

    def get_specific_days_posts(self, day, context="client"):
        responses = self.make_request("GET", "posts", {"day": day}, context)
        responses = responses["posts"]

        return helpers.parse_posts(responses)

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
        return helpers.parse_users(users["users"])

    def get_user(self, username, context="client"):
        user = self.make_request("GET", "users/%s" % username, None, context)
        return helpers.parse_users(user["user"])


def main():
    client_id = "35587d189b3370c86629d4ba77027cfcaa6130970e4d3217da383042450ff501"
    client_secret = "42a385e7aae68c1ef243ae2634864ee7bc0576f66550f22149d510173c728cd8"
    redirect_uri = "http://localhost:5000"

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)
    phc.oauth_client_token()


if __name__ == "__main__":
    main()
