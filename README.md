ph_py
=========
A Python wrapper for Product Hunt's REST API

Built by [Anat](https://twitter.com/anat_gilboa) and [Jasdev](https://twitter.com/jasdev)!

Installation
---
```python
pip install ph_py
```
Dependencies:
* requests
* simplejson

## Beta API Note

The Product Hunt API is in an early beta phase. As such, the official [docs] are super minimal. So, we implemented this library to the best of our knowledge.
Also, since write access to the API is currently restricted, we had to build functions with write functionality solely off the public documentation (**there may be bugs**).
If you find any issues, please submit a GitHub issue or a pull request!

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

### Error Handling
ProductHuntError is the general error handler with access to the error message and status code:

```python
try
    ...
except ProductHuntError as e
    print(e.error_message)
    print(e.status_code)
```

## Posts

- **Today's posts**

  Note: comments, votes, and related links only available when requesting a specific post)
  * Input:
      * *Optional*: `context`
  ```python
  get_todays_posts(context="client")
  ```
  * Output:
    * Array of [Post]s
- **Previous day's posts**
  * Input:
    * Required: `days_ago` (specify how many days ago, e.g. yesterday => 1)
    * *Optional*: `context`
  ```python
  get_previous_days_posts(days_ago, context="client")
  ```
  * Output:
    * Array of [Post]s
- **Specific day's posts**
  * Input:
    * Required: `day` (date in format of `"YYYY-MM-DD"`)
    * *Optional*: `context`
  ```python
  get_specific_days_posts(day, context="client")
  ```
  * Output:
    * [Post]
- **Details of a post**
  * Input:
    * Required: `post_id`
    * *Optional*: `context`
  ```python
  get_details_of_post(post_id, context="client")
  ```
  * Output:
    * [Post] (with [Comment]s, [Vote]s, and [Related Link]s)
- **Create a post**
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

- **Show Notifications**
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
- **Clear Notifications**
  ```python
  clear_notifications():
  ```
  * Output:
    * [Notification]s

## User

- **Get Users**
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
- **Get User**
  * Input:
    * Required: `username`
    * *Optional*: `context`
  ```python
  get_user(username, context="client"):
  ```
  * Output:
    * [User]

## Post Votes

- **Vote for a Post**
  * Input:
    * Required: `post_id`
  ```python
  create_vote(post_id)
  ```
  * Output:
    * [Vote]
- **Delete a Vote**
  * Input:
    * Required: `post_id`
  ```python
  delete_vote(post_id)
  ```
  * Output:
    * [Vote]
- **Delete a Vote**
  * Input:
    * Required: `post_id`
  ```python
  delete_vote(post_id)
  ```
  * Output:
    * [Vote]
- **See all votes for a Post**
  * Input:
    * Required: `post_id`
    * *Optional*: `older` (get only records older than the provided id)
    * *Optional*: `newer` (get only records newer than the provided id)
    * *Optional*: `per_page` (define the amount of records sent per call, max 100)
    * *Optional*: `order` (define the order you want to receive the records, does not affect older/newer behavior)
    * *Optional*: `context`
  ```python
  get_post_votes(post_id, older=None, newer=None, per_page=100, order=None, context="client"):
  ```
  * Output:
    * Array of [Vote]s
- **See all of a user's Votes**
  * Input:
    * Required: `user_id`
    * *Optional*: `older` (get only records older than the provided id)
    * *Optional*: `newer` (get only records newer than the provided id)
    * *Optional*: `per_page` (define the amount of records sent per call, max 100)
    * *Optional*: `order` (define the order you want to receive the records, does not affect older/newer behavior)
    * *Optional*: `context`
  ```python
  get_user_votes(user_id, older=None, newer=None, per_page=100, order=None, context="client"):
  ```
  * Output:
    * Array of [Vote]s

## Comments

- **Fetch a Post's Comments**
  * Input:
    * Required: `post_id`
    * *Optional*: `older` (get only records older than the provided id)
    * *Optional*: `newer` (get only records newer than the provided id)
    * *Optional*: `per_page` (define the amount of records sent per call, max 100)
    * *Optional*: `order` (define the order you want to receive the records, does not affect older/newer behavior)
    * *Optional*: `context`
  ```python
  get_comments(post_id, older=None, newer=None, per_page=100, order=None, context="client"):
  ```
  * Output:
    * Array of [Comment]s
- **Create a Comment (or comment reply)**
  * Input:
    * Required: `body`
    * Required: `post_id`
    * *Optional*: `parent_comment_id`
  ```python
  create_comment(body, post_id, parent_comment_id=None):
  ```
  * Output:
    * [Comment]
- **Update Comment**
  * Input:
    * Required: `body`
    * Required: `comment_id`
  ```python
  update_comment(body, comment_id):
  ```
  * Output:
    * [Comment]

## Related-Links

- **Create a Related-Link**
  * Input:
    * Required: `post_id`
    * Required: `url`
    * *Optional*: `title`
  ```python
  create_related_link(post_id, url, title=None):
  ```
  * Output:
    * [Related Link]
- **Update a Related-Link**
  * Input:
    * Required: `post_id`
    * Required: `related_link_id`
    * Required: `title`
  ```python
  update_related_link(post_id, related_link_id, title):
  ```
  * Output:
    * [Related Link]
- **Delete Related-Link**
  * Input:
    * Required: `body`
    * Required: `related_link_id`
  ```python
  delete_related_link(post_id, related_link_id):
  ```
  * Output:
    * [Related Link]

[app dashboard]:https://www.producthunt.com/v1/oauth/applications
[Post]:https://github.com/anatg/ph_py/blob/master/ph_py/models/post.py
[Comment]:https://github.com/anatg/ph_py/blob/master/ph_py/models/comment.py
[Vote]:https://github.com/anatg/ph_py/blob/master/ph_py/models/vote.py
[Related Link]:https://github.com/anatg/ph_py/blob/master/ph_py/models/related_link.py
[Notification]:https://github.com/anatg/ph_py/blob/master/ph_py/models/notification.py
[User]:https://github.com/anatg/ph_py/blob/master/ph_py/models/user.py
[docs]:https://www.producthunt.com/v1/docs/
