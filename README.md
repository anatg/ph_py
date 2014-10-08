ph_py
=========
A Python wrapper for Product Hunt's REST API

Installation
---
```python
pip install ph_py
```
Dependencies:
* requests
* simplejson

Authentication
---
Product Hunt's API uses the OAuth2 protocol for authentication.

### Obtaining app credentials


  - Create your app via the [app dashboard]
  - Obtain an API Key and API Secret by entering your application name and redirect URI

### Using the ProductHuntClient class
Once you have your app credentials, you can pass them to the ProductHuntClient initializer. If your code is open source,
make sure to remove the credentials to prevent others from using them. Environment variables can help with this.

The library will automatically obtain a client token upon initialization.
```python
from ph_py import ProductHuntClient

client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
redirect_uri = "http://localhost:5000"

phc = ProductHuntClient(client_id, client_secret, redirect_uri)

# Example request
for post in phc.get_todays_posts():
    print(post.tagline)
```

### User Authorization
In order to authenticate using OAuth2, the user must authorize your app. To accomplish this flow, we've built some nice wrappers!

```python
import webbrowser
from ph_py import ProductHuntClient

client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
redirect_uri = "http://localhost:5000"
phc = ProductHuntClient(client_id, client_secret, redirect_uri)

webbrowser.open(phc.build_authorize_url())
code = Input("What is the code? ") # Python 3x
#code = raw_Input("What is the code? ") # Python 2x

# Sets user auth
phc.oauth_user_token(code)

user_details = phc.get_current_user_details()
print(user_details.email)
```

Note: if you have a developer token, you can optionally initialize with it as well (skipping authorization step).
```python
from ph_py import ProductHuntClient

client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
redirect_uri = "http://localhost:5000"
dev_token = YOUR_DEV_TOKEN

phc = ProductHuntClient(client_id, client_secret, redirect_uri, dev_token)

user_details = phc.get_current_user_details()
print(user_details.email)
```

#### Context
`context` is passed around in many of the ProductHuntClient functions as an optional parameter. The context may be either a `"client"` or `"user"`.
This specifies from which context the request should be made. The default is `"client"`, except for endpoints take actions on or about a specific user.

## Posts

- ### Today's posts
  Note: comments, votes, and related links only available when requesting a specific post)
    * Input:
        * *Optional*: `context`
```python
get_todays_posts(context="client")
```
  * Output:
    * Array of [Post]s
- ### Previous day's posts
  * Input:
    * Required: `days_ago` (specify how many days ago, e.g. yesterday => 1)
    * *Optional*: `context`
```python
get_previous_days_posts(days_ago, context="client")
```
  * Output:
    * Array of [Post]s
- ### Specific day's posts
    * Input:
        * Required: `day` (date in format of `"YYYY-MM-DD"`)
        * *Optional*: `context`
```python
get_specific_days_posts(day, context="client")
```
    * Output:
        * [Post]
- ### Details of a post
    * Input:
        * Required: `post_id`
        * *Optional*: `context`
```python
get_details_of_post(post_id, context="client")
```
    * Output:
        * [Post] (with [Comment]s, [Vote]s, and [Related Link]s)
- ### Create a post (requires write access to API)
    * Input:
        * Required: `url`
        * Required: `name` (name of the product)
        * Required: `tagline` (tagline of the product)
```python
create_a_post(url, name, tagline)
```
    * Output:
        * [Post]

## Notifications

- ### Show Notifications
  * Input:
    * *Optional*: `older` (get only records older than the provided id)
    * *Optional*: `newer` (get only records newer than the provided id)
    * *Optional*: `per_page` (define the amount of records sent per call, max 100)
    * *Optional*: `order` (define the order you want to receive the records, does not affect older/newer behavior)
```python
show_notifications(older=None, newer=None, per_page=100, order=None)
```
  * Output:
    * Array of [Notification]s
- ### Clear Notifications (requires write access to API)
```python
clear_notifications():
```
  * Output:
    * ([Docs](https://api.producthunt.com/v1/docs/notifications/notificationsdestroy__clear_your_notifications_count) state [Notification]s are returned, but can't verify without write access :pensive:)

## User

- ### Get Users
  * Input:
    * *Optional*: `older` (get only records older than the provided id)
    * *Optional*: `newer` (get only records newer than the provided id)
    * *Optional*: `per_page` (define the amount of records sent per call, max 100)
    * *Optional*: `order` (define the order you want to receive the records, does not affect older/newer behavior)
    * *Optional*: `context`
```python
get_users(older=None, newer=None, per_page=100, order=None, context="client")
```
  * Output:
    * Array of [User]s
- ### Get User
  * Input:
    * Required: `username`
    * *Optional*: `context`
```python
get_user(username, context="client"):
```
  * Output:
    * [User]


[app dashboard]:https://www.producthunt.com/v1/oauth/applications
[Post]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/post.py
[Comment]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/comment.py
[Vote]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/vote.py
[Related Link]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/related_link.py
[Notification]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/notification.py
[User]:https://github.com/Jasdev/ph_py/blob/master/ph_py/models/user.py
