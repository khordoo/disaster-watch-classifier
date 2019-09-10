# Disaster Watcher 

## Disaster Identification using Tweeter Data and Deep Learning
This repository contains the code for automatically identifying and classifying the disaster related tweets. The model is implemented using a Deep learning approach. 

## 1. Introduction
Social media is increasingly being used to broadcast useful information during local crisis situations(e.g. hurricanes, earthquakes, explosions, bombings,etc).Identifying disaster related information in social media is challenging due to the low signal-to-noise ratio.In this work we will use NLP to address this challenge.

Some of the tweets sent from mobile devices can be geotagged containing the precise location coordinates. However, only about 1% to 3% of all tweets are geotagged.Identifying the disaster related tweets along with their is highly valuable to for the first responders in the disaster and crisis situations. In this project we fist. identify the disaster related tweets from a deep learning model and then use Named Entity Recognition library to identify and map the location of the data.

## 2. Data
The natural disaster events generally generate a massive and disperse reaction in social media channels.Users usually express their thoughts and actions taken before, during, and after the storm. We used the classified crisis related tweets collection from the CrisisLex.org which is a repository of crisis-related social media data. We used the CrisisLexT6 dataset which includes Tweets from 6 crises, labeled by relatedness.

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
