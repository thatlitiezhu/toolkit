#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'consumer_key'#keep the quotes, replace inside with your consumer key
CONSUMER_SECRET = 'consumer_secret'#keep the quotes, replace inside with your consumer secret key
ACCESS_KEY = 'access_key'#keep the quotes, replace inside with your access token
ACCESS_SECRET = 'access_secret'#keep the quotes, replace inside with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweet = "It is " + time.ctime() + " in Troy, NY now :)" 
api.update_status(tweet)
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
#time.sleep(1800)
