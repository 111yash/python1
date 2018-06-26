#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
An access token is an object that describes the security context of a process or thread. 
The information in a token includes the identity and privileges of  the user account associated with the process or thread. ...
The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.


consumer_key11='vwdqsgjcvjabsncvvnmsxvs99'
consumer_secrete11='xshfxhg99lhfsbsvffgswgf1hdsghfgkhufteeryyi99'
access_token11='dsnxjwsdghjknbvffrddhjjjkjgdddghjjfg1'
access_token_secre11='bswhvwhvdwhsvhjwdsc33'





#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.


C:\Users\Dell>nslookup  google.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4002:803::200e
          172.217.161.14


C:\Users\Dell>nslookup  youtube.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    youtube.com
Addresses:  2404:6800:4002:807::200e
          172.217.24.238


C:\Users\Dell>nslookup  facebook.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35


C:\Users\Dell>nslookup  istragram.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    istragram.com
Addresses:  2a03:2880:f02f:f:face:b00c:0:2
          157.240.16.16

#Q.3- Using Tweepy library try to extract tweets from Twitter. 

import tweepy


consumer_key11=''
consumer_secrete11=''
access_token11=''
access_token_secret11=''
auth=tweepy.OAuthHandler(consumer_key11,consumer_secrete11)
auth.set_access_token(access_token11,access_token_secret11)
api=tweepy.API(auth)
tweets=api.search("#notwithoutmydog",lang="en",count="5",tweet_mode="extended")

#print(tweets)


for tweet in tweets:
    print("-----------------")
    print(tweet.full_text)
    print("-----------------------")

	
	
	
	
	
	
	
	
	
#.4- What is a difference between library and API . Figure it out with examples.
	LIBRARY
	A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
     Library:

is Reusable set of code or compilation of set of things which you may need in order to  ease your process of development, ex: JQuery library, is a library of prewritten, cross-browser Javascript animations and functions which you will need while making a website.
	
	
	
	API(application programming interface)
An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)

API (Application Programming Interface):

It is interface with which you can access any Application's features, without hosting it on your server, ex: with Google Map APIs you can show maps for different places without writing/hosting the whole code on your server, and just use it, usually this data transfer is in form of JSON i.e JavaScript Object Notation.

SDK (Software Development Kit):

example= date today =new date()