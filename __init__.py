from flask import render_template, request
from CTFd.models import db, Challenges, Files, Solves, WrongKeys, Keys, Tags, Teams, Awards, Hints, Unlocks
from CTFd import utils

from CTFd.plugins.DynamicValueChallenge import DynamicValueChallenge
from CTFd.plugins.challenges import CHALLANGE_CLASSES

import tweepy

#You have to create a credentials.py file with your tokens and secrets in it
from credentials import *

AUTH = None
API = None

class TweetDaChallenge(DynamicValueChallenge):
	id = "tweetnamic"
	name = "tweetnamic"

	@staticmethod
	def create(request):
		return DynamicValueChallenge.create(request)

	@staticmethod
	def read(challenge):
		return DynamicValueChallenge.read(challenge)

	@staticmethod
	def update(challenge, request):
		return DynamicValueChallenge.update(challenge, request)

	@staticmethod
	def delete(challenge):
		return DynamicValueChallenge.delete(challenge)

	@staticmethod
	def attempt(challenge, request):
		return DynamicValueChallenge.attempt(challenge, request)

	@staticmethod
	def solve(team, chal, request):
		
		user = Teams.query.filter_by(id=team.id).first_or_404()
		score = user.score(admin=True)

		tweet = team.name + " just solved " + chal.name + " and now has " + score + " points! #kdctf #challengesolved"
		API.update_status(status=tweet)

		return DynamicValueChallenge.solve(team, chal, request)

	@staticmethod
	def solve(team, chal, request):
		return DynamicValueChallenge.fail(team, chal, request)

def load(app):
	AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	API = tweepy.API(AUTH)
    CHALLENGE_CLASSES['tweetnamic'] = TweetDaChallenge
