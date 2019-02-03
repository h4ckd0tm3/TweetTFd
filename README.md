# TweetTFd

This is a plugin for the popular jeopardy CTF platform [CTFd](https://github.com/CTFd/CTFd) it requires the python module tweepy. This is completly based on the [Dynamic Scoring](https://github.com/CTFd/DynamicValueChallenge) plugin!

It creates a new challenge type that tweets whenever a team solves a challenge :)

You need to create a credentials.py file to use this plugin!
credentials.py example:

```
CONSUMER_KEY = 'YOUR APP KEY'
CONSUMER_SECRET = 'YOUR APP SECRET'
ACCESS_TOKEN = 'ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS TOKEN SECRET'
```