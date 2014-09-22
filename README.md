ph_py
=========
A Python wrapper for Product Hunt's REST API

Installation
---
```python
pip install alephnull
```
Requires
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


```python
    client_id = YOUR_CLIENT_ID
    client_secret = YOUR_CLIENT_SECRET
    redirect_uri = "http://localhost:5000"

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)

```

Note: if you have a

From here, you'll need to either obtain a client or user token.  See below:

### Authorization
In order to authenticate using OAuth2, the user must authorize your app. To help with this step, we've built a function
to build the authorization url.

```python
phc.build_authorize_url()
```

and enter it as a "client" or a "user":
```python
code = "CODE_RETURNED_IN_BROWSER"
    phc.oauth_user_token(code)
    phc.oauth_client_token()
```
#### Context
```"context"``` is passed around in many of the fucntions as an optional parameter. The context may be either a ```"client"``` or ```"user"```. All functions involving "context" default to "client" unless otherwise specified

##Posts

###GET:

- ####Today's posts
    * INPUT: 
        * *Optional* :context
```python
phc.get_todays_posts(context="client")
```
    * OUTPUT:
        * today's posts
        
- ####Previous day's posts 
    * INPUT: 
        * ```days_ago```: specify how many days ago (yesterday = 1)
        * *Optional* :context
```python
phc.get_previous_days_posts(days_ago, context="client")
```
    * OUTPUT:
        * previous day's posts
        
- ####Specific day's posts
    * INPUT:
        * ```day```: date in format of ```"YYYY-MM-DD"```
        * *Optional* :context
```python
phc.get_specific_days_posts(day, context="client")
```

    * OUTPUT:
        * specific days posts
        
- ####Details of a post

    * INPUT:
        * ```post_id```: post's id
        * *Optional* :context    
```python
phc.get_details_of_post(post_id, context="client")
```
    * OUTPUT:
        * details of a post
        
###POST:

- ####Create a post
    * INPUT:
        * ```url```: url to post
        * ```name```: name of the product
        * ```tagline```: tagline of the product
```python
phc.create_a_post(url, name, tagline)
```
    * OUTPUT:
        * status code(201 if created)

##Notifications

###GET:

- ####Show notifications
    * INPUT:
        * *Optional*: older
        * *Optional*: newer
        * *Optional*: per_page (>= 100)
        * *Optional*: order

```
phc.show_notifications(older=None, newer=None, per_page=100, order=None)
```
    * OUTPUT:
        * authenticated user's notifications


###DELETE:

- #### Clear notifications
    * INPUT: (none)
```
phc.clear_notifications()
```
    * OUPUT:
        * status code (200 if successfully deleted)


##User

###GET:
- ####Get all users
    * INPUT:
        * *Optional*: older
        * *Optional*: newer
        * *Optional*: per_page (>= 100)
        * *Optional*: order
        * *Optional*: context
    
```
phc.get_users(older=None, newer=None, per_page=100, order=None, context="client") 
```
* OUTPUT:
    * all of PH's users

- ####Get a specific user
    * INPUT: 
        * ```username```
        * *Optional*: context
```python
phc.get_user(username, context="client")
```
    * OUTPUT:
        * a specific user

##Votes

###GET
- ####Get a user's votes
    *INPUT
        * ```user_id```
        * *Optional*: older
        * *Optional*: newer
        * *Optional*: per_page (>= 100)
        * *Optional*: order
        * *Optional*: context
```python
ghc.get_user_votes(user_id, older=None, newer=None, per_page=100, order=None, context="client")
```
    *OUTPUT
        * all of a user's votes

- ####Get a post's votes
    * INPUT
        * ```post_id```
        * *Optional*: older
        * *Optional*: newer
        * *Optional*: per_page (>= 100)
        * *Optional*: order
        * *Optional*: context

```python
phc.get_post_votes(post_id, older=None, newer=None, per_page=100, order=None, context="client")
```
    * OUTPUT:
        * all of a post's votes

###POST
- ####Create a vote
    * INPUT
        * ```post_id```

```python
phc.create_vote(post_id)
```
    * OUTPUT
        * a vote


###DELETE
- ###Delete a vote
    *INPUT
        * ```post_id```
```python
phc.delete_vote(post_id)
```
    *OUTPUT
        * deleted vote



[app dashboard]:https://www.producthunt.com/v1/oauth/applications
