__author__ = 'ag'

class Post:

    def __init__(self, id, name, tagline, created_at, day, comments_count, votes_count, discussion_url, redirect_url, screenshot_url, maker_inside):
        "id": id,
        "name": name,
        "tagline": tagline,
        "created_at": created_at,
        "day": "2014-08-22",
        "comments_count": 0,
        "votes_count": 1,
        "discussion_url": "http://www.producthunt.com/posts/awesome-idea-16",
        "redirect_url": "http://www.producthunt.com/l/56ffec54c1/1",
        "screenshot_url": {
                              "300px": "http://placehold.it/400x400",
                              "850px": "http://placehold.it/400x400"
                          },
        "maker_inside": false,