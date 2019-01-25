'''
__author__ = "Chandramohan Jagtap"
__license__ = "GPL"
__email__ = "cmjagtap1@gmail.com"
__Date__ = "24-1-2019"

'''

import twitter      #import library
from elasticsearch import Elasticsearch

def authenticateUser(userName):
    #follwing is api keys provide your keys to run this project
    consumer_key=''
    consumer_secret=''
    access_token_key=''
    access_token_secret=''
    
    api = twitter.Api(consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret)
    
    #print(api.VerifyCredentials())

    latestTweets = api.GetUserTimeline(screen_name = userName) #read latest  tweets
    tweets = [i.AsDict() for i in latestTweets]
    
    tweetList=[]
    for t in tweets:
        parseTweets={}
        parseTweets[t['id']]=(t['created_at'],t["text"])
        tweetList.append(parseTweets)
    return tweetList



def createIndexDumpData(latestT):
    for i in range(1,len(latestT)):
        #created index and dump tweets into same index
        es.index(index="donald",ignore=400,doc_type='docs',body=latestT[i-1],id=i) 
        
        #es.indices.get_mapping(index="donald",doc_type="docs") #to check is mapping done

def getRecord(idx):
    result = es.get(index="donald",doc_type="docs",id=idx) #find tweet given by id

    return result


es = Elasticsearch() #create Object of elastic Search default host=localhost and port is port:9200

latestT=authenticateUser("realDonaldTrump") #authenticate user and provide twitter username to find tweets

createIndexDumpData(latestT) #build and dump tweets into elasticsearch

print (getRecord(1)) #provide id to get record
