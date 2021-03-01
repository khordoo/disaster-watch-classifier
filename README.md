# Disaster Watcher 

## Disaster Identification using Tweeter Data and Deep Learning
This repository contains the code for automatically identifying and classifying the disaster related tweets. The model is implemented using a Deep learning approach. 

## 1. Introduction
Social media is increasingly being used to broadcast useful information during local crisis situations(e.g. hurricanes, earthquakes, explosions, bombings,etc).Identifying disaster related information in social media is challenging due to the low signal-to-noise ratio.In this work we will use NLP to address this challenge.

Some of the tweets sent from mobile devices can be geotagged containing the precise location coordinates. However, only about 1% to 3% of all tweets are geotagged. Identifying the disaster-related tweets along with their actual geolocations is highly valuable for the first responders in disaster and crisis situations. In this project, we first identify the disaster-related tweets using a deep learning model and subsequently use a Named Entity Recognition model to identify and extract the name of the places (cities, countries, etc.) from the tweets, and finally use a geoparser model to identify the geo-location of the events on the map. We should emphesis that geo-location identification is a critical step as we can not simply use the location of the tweets provided by the tweeter API for disaster identification purposes. The location of the person who tweets about a disaster is not necessarily identical to the actual location of the events. A user could be located in Vancouver but tweets about a flood happening in another city like Calgary.  

## 2. Data
Natural disaster events generally generate massive and disperse reactions in social media channels. Users usually express their thoughts and actions taken before, during, and after the events such as floods, storm, wilfires, etc. We used the classified crisis related tweets collection from the CrisisLex.org which is a repository of crisis-related social media data. We used the CrisisLexT6 dataset which includes Tweets from 6 crises, labeled by relatedness.

Contents: ~60K tweets posted during 6 crisis events in 2012 and 2013.
Labels: ~60,000 tweets (10,000 in each collection) were labeled by crowdsourcing workers according to relatedness (as "on-topic", or "off-topic").
The data from the following crisis events were used in this analysis :

- Flood
- Earthquake
- Hurricane
- Tornado
- Explosion
- Bombing
- Wildfire

## 3. Application
The workflow starts with the data collection process. The backend API uses a keyword-based sampling approach to collect tweets using Twitter’s streaming API. In this context, a reference dictionary of disaster-related terms, developed by CrisisLex.org, was used as keywords. CrisisLex is a lexicon of 380 disaster-related terms that frequently appeared in relevant tweets during different types of disasters between October 2012 and July 2013 in the US, Canada, and Australia.

The API then sends the tweet to the deep learning model built using TensorFlow 2.0 for Python and exposed as a Flask app. The model analyzes textual content of tweets to evaluate their relevance to floods, earthquakes, hurricanes, tornadoes, explosions, and bombings. The relevant tweets are then sent to the geoparser, which extracts place names from the text and geocodes them. Finally, the results are sent to the frontend for visualization.
You can read the full description of the application along with the arcitectral diangram on [Google's Tensorflow blog.](https://blog.tensorflow.org/2019/09/disaster-watch-crisis-mapping-platform.html)


![image](https://user-images.githubusercontent.com/32692718/78304887-e6bdcb00-74fc-11ea-939d-19b6334edd5e.png)



