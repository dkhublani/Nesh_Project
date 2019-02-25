# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:58:26 2019

@author: Shiva
"""

import pandas as pd
from AdvancedAnalytics import Sentiment
from sklearn.feature_extraction.text import CountVectorizer
from news_articles import scrape_all_articles

#Create Word Frequency by Review Matrix using Custom Analyzer
sa = Sentiment(n_terms=4)
cv = CountVectorizer(max_df=1.0, min_df=1, max_features=None, \
                     preprocessor=sa.preprocessor, \
                     ngram_range=(1,2))

def stock_sentiment(company):
    company_articles = scrape_all_articles('company' , 1)
    df_company = pd.DataFrame(company_articles, columns = ['company'])
    tf = cv.fit_transform(df_company['company'])
    terms = cv.get_feature_names()
    n_reviews = tf.shape[0]
    n_terms = tf.shape[1]
    print('{:.<22s}{:>6d}'.format("Number of Reviews", n_reviews))
    print('{:.<22s}{:>6d}'.format("Number of Terms", n_terms))
    sentiment_score = sa.scores(tf, terms)
    return sentiment_score

if __name__ == "__main__":
    x = input("Enter the ticker of the company in inverted commas:")
    stock_sentiment(x)
