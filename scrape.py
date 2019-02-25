# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:26:56 2019

@author: Shiva
"""

from lxml import html
import requests
from time import sleep
import json
import argparse
from random import randint

def parse_finance_page(ticker):
  """
  Grab financial data from NASDAQ page
  
  Args:
    ticker (str): Stock symbol
  
  Returns:
    dict: Scraped data
  """
  key_stock_dict = {}
  headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
        "Connection":"keep-alive",
        "Host":"www.nasdaq.com",
        "Referer":"http://www.nasdaq.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
  }

  # Retrying for failed request
  for retries in range(5):
    try:    
      url = "http://www.nasdaq.com/symbol/%s"%(ticker)
      response = requests.get(url, headers = headers, verify=False)
      
      if response.status_code!=200:
        raise ValueError("Invalid Response Received From Webserver")

      print("Parsing %s"%(url))
      # Adding random delay
      sleep(randint(1,3))   
      parser = html.fromstring(response.text)
      xpath_head = "//div[@id='qwidget_pageheader']//h1//text()"
      xpath_key_stock_table = '//div[@class="row overview-results relativeP"]//div[contains(@class,"table-table")]/div'
      xpath_key = './/div[@class="table-cell"]/b/text()'
      xpath_value = './/div[@class="table-cell"]/text()'
      xpath_present_value="//div[@id='qwidget_lastsale']//text()"

      raw_name = parser.xpath(xpath_head)
      key_stock_table =  parser.xpath(xpath_key_stock_table)
      raw_current_value = parser.xpath(xpath_present_value)

      company_name = raw_name[0].replace("Common Stock Quote & Summary Data","").strip() if raw_name else ''

      # Grabbing ans cleaning keystock data
      for i in key_stock_table:
        key = i.xpath(xpath_key)
        value = i.xpath(xpath_value)
        key = ''.join(key).strip() 
        value = ' '.join(''.join(value).split()) 
        key_stock_dict[key] = value

      nasdaq_data = {

              "company_name":company_name,
              "ticker":ticker,
              "url":url,
              "current_value": raw_current_value,
              "key_stock_data":key_stock_dict
      }
      return nasdaq_data

    except Exception as e:
      print("Failed to process the request, Exception:%s"%(e))

if __name__=="__main__":

  argparser = argparse.ArgumentParser()
  argparser.add_argument('ticker',help = 'Company stock symbol')
  args = argparser.parse_args()
  ticker = args.ticker
  print("Fetching data for %s"%(ticker))
  scraped_data = parse_finance_page(ticker)
  print("Writing scraped data to output file")

  with open('%s-summary.json'%(ticker),'w') as fp:
    json.dump(scraped_data,fp,indent = 4,ensure_ascii=False)