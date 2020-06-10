# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:46:37 2020

@author: HP
"""

#Importing Libraries
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

#For my example I've used folloeing dates
begin_date = dt.date(2019,8,12)
end_date = dt.date(2019,9,12)

#No of tweets and language
limit=1000
lang='english'

#Main body
tweets = query_tweets("Hello", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)

df=pd.DataFrame(t.__dict__ for t in tweets)

