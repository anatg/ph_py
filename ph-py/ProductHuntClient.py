__author__ = 'ag'

import requests as r

class ProductHuntClient:
    API_BASE = "https://api.producthunt.com/v1/"

    def __init__(self, client_id, client_secret, redirect_uri, dev_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.dev_token = dev_token
        self.redirect_uri = redirect_uri
        self.user_auth = None
        self.client_auth = None


    def build_authorize_url(self):
        url = self.API_BASE + "oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code&scope=public private"%(self.client_id, self.redirect_uri)
        return url

    def oauth_user_token(self, code):
        data = {
            "client_id" : self.client_id,
            "client_secret" : self.client_secret,
            "redirect_uri" : self.redirect_uri,
            "grant_type" : "authorization_code",
            "code" : code
        }
        response = self.make_request("POST", "oauth/token", data)

        self.user_auth = response
        return self.user_auth

    def oauth_client_token(self):
        data = {
            "client_id" : self.client_id,
            "client_secret" : self.client_secret,
            "grant_type" : "client_credentials"
        }
        response = self.make_request("POST", "oauth/token", data)

        self.client_auth = response
        return self.client_auth


    #method is the type, route is where it's going, data is query params or form data
    def make_request(self, method, route, data):
        url = self.API_BASE + route

        if method == "GET":
            pass
        elif method == "POST":
            response = r.post(url, data=data)


        return response.json()



def main():

    client_id = "35587d189b3370c86629d4ba77027cfcaa6130970e4d3217da383042450ff501"
    client_secret = "42a385e7aae68c1ef243ae2634864ee7bc0576f66550f22149d510173c728cd8"
    redirect_uri = "http://localhost:5000"

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)
    print phc.build_authorize_url()
    print phc.oauth_client_token()


if __name__ == "__main__":
    main()