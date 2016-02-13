import random													
import math
import sys
import string
import re
import time
import pickle
from operator import itemgetter
from collections import Counter

tweetIndex=[]
hashtag=""

def extractHashtagsFromTweets(tweet):
	hashtagSet = []
	keywordSet=[]

	for word in tweet.split(' '):
			if word.startswith('#'):
				hashtagSet.append(word)
			else: 
				keywordSet.append(word)
	return hashtagSet,keywordSet

def extractWordsFromTweets(tweet):
	totalwords = []
	f=open("sample_tweets.txt","r")
	with open("sample_tweets.txt","r") as f:
		for line in f: 
			for word in line.split():
				totalwords.append(word)
	return totalwords

def getIndexofTweet(tweet_word):
	index1=0
	for i in range(0,len(tweetIndex)):
		if (tweet_word==tweetIndex[i][0]):
			index1= i
	existing_hashtags=tweetIndex[index1][1]
	return index1

def checkKeys(each_word):
	index =-1
	list=map(itemgetter(0), tweetIndex)
	
	if each_word in list:
		index =list.index(each_word)
	return index

def AppendRepeated(index,hashtags):
	tweetIndex[index][1]=tweetIndex[index][1]+hashtags

def createHashMap(filename):
	hashtags=[]
	keywords=[]
	with open(filename,"r") as f:
		for line in f:
			hashtags,keywords=extractHashtagsFromTweets(line)

			for each_words in keywords:
				each_words=each_words.lower()	
				if len(tweetIndex)!=0:
					index=checkKeys(each_words)
					if index!=-1:
						AppendRepeated(index,hashtags)	
					else:
						oneline=[each_words]
						oneline.append(hashtags)
						tweetIndex.append(oneline)
				else:
					oneline=[each_words]
					oneline.append(hashtags)
					tweetIndex.append(oneline)	
		return tweetIndex

def getTotalHashtagCount(keyword):
	UniqueHashtagSet= []
	index=getIndexofTweet(keyword)
	hashtagSet=tweetIndex[index][1]
	return len(hashtagSet)

def getIndividualHashtagCount(keyword):
	index=checkKeys(keyword)
	hashtagSet=tweetIndex[index][1]
	count=Counter(hashtagSet)
	count=Counter(hashtagSet).most_common(1)
	return count

def getFourHashtags(tweet):
	hashtagPredict=[]
	eachHashtagCount=[]

	for word in tweet.split(' '):
		word=word.lower()
		#print word
		eachHashtagCount=getIndividualHashtagCount(word)
		hashtagPredict.append(eachHashtagCount[0][0]) 

	return hashtagPredict


	#keyword_track=Counter(hashtagCount)
	#keyword_track=Counter(hashtagCount).most_common(1)
	#return keyword_track



def getMoreHashtags(tweet):
	hashtagCount=[]
	tweet1=[]
	maxfour=[]
	for keyword in tweet.split(' '):
		#print keyword
		hashset=getTotalHashtagCount(keyword)
		oneline=[keyword]
		oneline.append(hashset)
		hashtagCount.append(oneline)
		sorted(hashtagCount,key=itemgetter(1))
	#print hashtagCount
	for i in range(0,4):
		tweet1.append(hashtagCount[i][0])
		new_tweet=" ".join(tweet1)
	hashtagPredict=getFourHashtags(new_tweet)
	predictedValues=set(hashtagPredict)
	return predictedValues

#MAIN PROGRAM						

hashtag=[]
uniqueHashtagSet= []
eachHashtagCount=[]
hashtagPredict=[]

totalWords=[]
tweetWords=[]

tweetIndex=createHashMap("C:\Users\Tanushree\Desktop\SMM\Projects\hashTagPrediction\preprocessed\pre_processed_dataTaining.txt")
#print tweetIndex
#tweet="declared invasion sex role told issue"
#hashtagPredict=getMoreHashtags(tweet)
#print hashtagPredict


fopen = open("sample_tweets.txt")
#for line in reader:
#reader=fopen.readline()
for line in fopen:
	hashtagPredict=getMoreHashtags(line)
	print hashtagPredict
	print line


