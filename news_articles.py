# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:16:04 2019

@author: 19797
"""

'''load packages'''
import requests
from bs4 import BeautifulSoup
 
'''Generalized function to get all news-related articles from a Nasdaq webpage'''
def get_news_urls(links_site):
    '''scrape the html of the site'''
    resp = requests.get(links_site)
 
    if not resp.ok:
        return None
 
    html = resp.content
 
    '''convert html to BeautifulSoup object'''
    soup = BeautifulSoup(html , 'lxml')
 
    '''get list of all links on webpage'''
    links = soup.find_all('a')
 
    urls = [link.get('href') for link in links]
    urls = [url for url in urls if url is not None]
 
    '''Filter the list of urls to just the news articles'''
    news_urls = [url for url in urls if '/article/' in url]
 
    return news_urls

def scrape_news_text(news_url):
 
    news_html = requests.get(news_url).content
 
    '''convert html to BeautifulSoup object'''
    news_soup = BeautifulSoup(news_html , 'lxml')
 
    paragraphs = [par.text for par in news_soup.find_all('p')]
    news_text = '\n'.join(paragraphs)
 
    return news_text

def scrape_all_articles(ticker , upper_page_limit = 1):
 
    landing_site = 'http://www.nasdaq.com/symbol/' + ticker + '/news-headlines'
 
    all_news_urls = get_news_urls(landing_site)
 
    current_urls_list = all_news_urls.copy()
 
    index = 2
 
    '''Loop through each sequential page, scraping the links from each'''
    while (current_urls_list is not None) and (current_urls_list != []) and \
        (index <= upper_page_limit):
 
        '''Construct URL for page in loop based off index'''
        current_site = landing_site + '?page=' + str(index)
        current_urls_list = get_news_urls(current_site)
 
        '''Append current webpage's list of urls to all_news_urls'''
        all_news_urls = all_news_urls + current_urls_list
 
        index = index + 1
 
    all_news_urls = list(set(all_news_urls))
 
    '''Now, we have a list of urls, we need to actually scrape the text'''
    all_articles = [scrape_news_text(news_url) for news_url in all_news_urls]
    return all_articles

if __name__=="__main__":
    OXY_articles = scrape_all_articles('OXY' , 1)[3]
    EOG_articles = scrape_all_articles('EOG' , 1)[1]
    APA_articles = scrape_all_articles('APA' , 1)[0]
    APC_articles = scrape_all_articles('APC' , 1)[2]
    COP_articles = scrape_all_articles('COP' , 1)[4]
    
    OXY_file = open("OXY_news.txt","w")
    OXY_file.write(OXY_articles)
    OXY_file.close()
    
    EOG_file = open("EOG_news.txt","w")
    EOG_file.write(EOG_articles)
    EOG_file.close()

    APA_file = open("APA_news.txt","w")
    APA_file.write(APA_articles)
    APA_file.close()

    APC_file = open("APC_news.txt","w")
    APC_file.write(APC_articles)
    APC_file.close()

    COP_file = open("COP_news.txt","w")
    COP_file.write(COP_articles)
    COP_file.close()

