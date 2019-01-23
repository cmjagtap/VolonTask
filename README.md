# Twitter API and Elasticsearch

#### AUTHOR:

- [Chandramohan Jagtap](https://github.com/cmjagtap "Chandramohan's github profile")


#### DESCRIPTION:

  - Dataset:  
        Collected latest tweets from tweeter using API.

  - Data Pre-processing:  
        From collected data i have separted tweet id, tweet date time and text of tweet

  - Tasks:  
        Find out donald trump latest tweets using twitter API and dump them into elasticsearch
  
  - Solution: 
        I have design module for genral use we can find any twitter account tweets by providing username to 
        authenticateUser() method and follwing are sub-task done.
        1) Authenticate user via API.
        2) get Tweets from api and created dictionary to store temporary.
        3) Created Indexing to map reocrds records and dump into elasticsearch.
        4) Retrived record using id.


#### Requirment:

        1) Install python3 
        2) python twitter package  install using :-	  ' pip3 install twitter '
		3) python Elasticsearch package install using:-  ' pip3 install elasticsearch '
        4) Java version <10 to run elasticsearch 


#### Execution :  
	  ` python3 getTweetsAndDumpElasticSearch.py `
