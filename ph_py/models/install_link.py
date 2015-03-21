class InstallLink:

    def __init__(self, platform, created_at, redirect_url, post_id):
        self.redirect_url = redirect_url
        self.platform = platform
        self.created_at = created_at
        self.post_id = post_id