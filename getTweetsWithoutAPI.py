'''
__author__ = "Chandramohan Jagtap"
__license__ = "GPL"
__email__ = "cmjagtap1@gmail.com"
__Date__ = "31-1-2019"

Task: get tweets without twitter API using selenium (web scraping ) and store it into elasticsearch. 

'''

from bs4 import BeautifulSoup    
from selenium import webdriver
from elasticsearch import Elasticsearch

def creatConnection(username):
    driverObject = webdriver.Chrome()
    base_url = 'http://twitter.com/' 
    url = base_url + username
    driverObject.get(url)
    
    return driverObject

def parseHtmlPage(driverObject):
    soup=BeautifulSoup(driverObject.page_source, "lxml")
    
    alltweets = soup.findAll("div", {"class": "js-tweet-text-container"})

    tweetList=[]
    i=0
    for t in alltweets:
        parseTweets={}
        parseTweets[i]=(t.text)
        tweetList.append(parseTweets)
        i=i+1
    return tweetList

def createIndexDumpData(latestTweets):
    for index in range(1,len(latestTweets)):
        #created index and dump tweets into same index
        es.index(index="x-men",ignore=400,doc_type='docs',body=latestTweets[index-1],id=index) 

def getRecord(idx):
    result = es.get(index="x-men",doc_type="docs",id=idx) #find tweet given by id

    return result

driverObject = creatConnection("realDonaldTrump") #here we can take any username which we need to fetch tweets
latestTweets = parseHtmlPage(driverObject)

es = Elasticsearch()

createIndexDumpData(latestTweets)
print(getRecord(2)) #provide id to get record
print(getRecord(10)['_source'])
