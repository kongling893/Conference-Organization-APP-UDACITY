# Conference Organization APP using Google App Engine
This is the fourth project for "Full Stack Web Developer Nanodegree" on Udacity.

In this project, the cloud-based APIs are developed to support a provided conference organization application that exists on the web as well as a native Android application. Google Cloud Endpoints with Python is used to realize the API backend on Google APP Engine. 

The website is deployed on Google Cloud Platform: https://windy-bounty-94723.appspot.com/

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting
   your local server's address (by default [localhost:8080][5].)
1. Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool


## The Backend APIs



## Task 1: Add Sessions to a Conference
- Session Model 
	- Created as `ndb.Model`.
 	- Has the following attributes:
	```python
	class Session(ndb.Model):
		"""Session -- Session object"""
		name = ndb.StringProperty()
		highlights = ndb.StringProperty()
		speaker = ndb.StringProperty(required=True)  
		duration  = ndb.IntegerProperty() 
		typeOfSession  = ndb.StringProperty(repeated=True) 
		date = ndb.DateProperty()
		startTime = ndb.TimeProperty() 
		websafeConferenceKey =  ndb.StringProperty()
	```
- SessionForm 
	- Created as `messages.Message`.
	- Has the  attributes corresponding the ones in Session Model but sessionSafeKey is added. 	
	```python
	class SessionForm(messages.Message):
		"""SessionForm -- Session outbound form message"""
		name  = messages.StringField(1)
		highlights  = messages.StringField(2)
		speaker = messages.StringField(3)
		duration = messages.IntegerField(4)
		typeOfSession = messages.StringField(5, repeated=True)
		date  = messages.StringField(6) 
		startTime = messages.StringField(7) 
		sessionSafeKey  = messages.StringField(8)
		websafeConferenceKey  = messages.StringField(9)
	```

## Task 2: Add Sessions to User Wishlist


## Task 3: Work on indexes and queries

## Task 4: Add a Task
