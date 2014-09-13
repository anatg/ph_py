__author__ = 'ag'


class ProductHuntClient:
    API_base = "https://api.producthunt.com/v1/"

    def __init__(self, API_Key, API_Secret, redirect_uri, dev_token=None):
        self.api_key = API_Key
        self.api_secret = API_Secret
        self.dev_token = dev_token
        self.redirect_uri = redirect_uri

    def build_authorize_url(self):
        url = self.API_base + "oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code&scope=public private"%(self.api_key, self.redirect_uri)
        return url



def main():

    key = ""
    secret = ""
    redirect_uri = ""

    phc = ProductHuntClient(key, secret, redirect_uri)
    print phc.build_authorize_url()


if __name__ == "__main__":
    main()