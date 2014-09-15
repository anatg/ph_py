ph-py
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

### Obtaining an access token


  - Create your app via the [app dashboard]
  - Plug in your Redirect URI, API Key and API Secret

### Using an access token
Once you have an access token, you can pass that token into the Product Hunt Client constructor. When committing your work, though, make sure to remove the codes in order to not expose your custom application's credentials. 


```python
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    redirect_uri = "http://localhost:5000"

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)

```

In order to authenticate using OAuth 2, pass in the "code" generated in your favorite browser from
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
