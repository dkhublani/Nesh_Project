# Nesh_Project
Scrape information from a publicly available website to present insights about an Oil and Gas company

## From where
The objective of the project is to create a simple web interface where someone can search using  the Ticker Symbol or Name of a company and receive insights about the company. We used NASDAQ.com to extract stock price and other financial numbers.

API from Yahoo is used to extract the stock trends. We focused only on few companies in this project(OXY, EOG, APC, APA, COP and PXD) but any company can be added depending on the requirements just by using the corresponding ticker.

## Description

 Some basic insights are as follows:-
 
 * Last known stock price
 * Financial numbers like 1 year target, today's high/low, 52 week high/low and other relevant ket stock data from www.nasdaq.com
 * News articles published about the company. Sentiment analysis of the articles 
 * Stock price trend 
 
## How to run

### Run the command- 

* python -m pip install -r requirements.txt 

 OR

 pip install -r requirements.txt

 pip3/python3 according to the version of the python to install dependencies associated with the post

* python flask app.py

* Copy the server IP to any web browser

* Enter the ticker (OXY, EOG, APC, APA, COP and PXD) and hit submit button
 
* To plot the stock prices trend:
Open and run plot_stock.py python script in any IED
User inputs for the start date, end date and Ticker symbol is required. 
This script will plot and show the result based on the user requirements.

* To view the results of sentiment analysis of the above mentioned Oil and Gas companies:
Run the sentiment.py 
User input for the company name is required.
The script will carry out sentiment analysis on the news article related to the company which 
was scraped from nasdaq.com and provides the average as well as minimum and maximum sentiment 
scores.

## Description of files -

* Scrape.py-
Python script that scrapes stock data from NASDAQ
To execute it: 
python scrape.py “Ticker symbol of the company”
e.g – python scrape.py EOG
* flask_app.py –
python script that runs a flask app to host a local server and post the stock data along with the news articles related to it. 
There is a search bar on the home page that allows you to search for any (5 as of now) company of interest and the result will provide you all the data related to it’s stock and latest news (restricted to 1 but can be extended easily)
* news_articles.py:
scrapes news article related to the company of interest from Nasdaq.com. Ticker symbol of company is taken as an input the news article is returned as output. 
* plot_stock.py:
It fetches real time data from yahoo finance and returns plot of the trend of stock price for the company of interest. Time period and the ticker symbol is taken as user input and it returns the plot as an output. 
* Sentiment_analysis.py:
This script uses the news article related to the company and calculates the average/min/max sentiment of the text presented. 


## Further Improvements 

