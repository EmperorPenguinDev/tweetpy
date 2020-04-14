#!/usr/bin/env python
#Create by MrsIneffable
import sys, os, time
import tweepy
keys = dict(
consumer_key='5NXxgK2HYaMh3tiblwvBaCn6C',
consumer_secret='CFc3bdPKee0XT6HbwvujptT36GkddTkKEVflyt4fKOhRvEL0BW',
access_token='1232199623764131841-sLRKXjQqcU6u0kvmiZeYIpZNsafMUL', 
access_token_secret='2IiTPCzLRLN4FkUPvWhQB8UgHXXFgpgpmWSNtw9YwUCxb'
)

user = "@MrsIneffable"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	#ftweet = open("tweet.txt", "r")
	#fftweet = ftweet.read()
	message=input("tweet: ")
	imagepath=input("image: ")
	# api.update_status(message)
	# api.update_with_media(filename=imagepath,status=message,place_id='ce7988d3a8b6f49f') #indonesia
	api.update_with_media(filename=imagepath,status=message,place_id='06ef846bfc783874') #japan
	time.sleep(1000)
	# , lat = '36.2048', long = '138.2529'

if __name__ == "__main__":
	while 1:
		tweet()