import urllib.request,json
from .models import News
import datetime
from datetime import datetime, timezone

base_url = 'https://newsapi.org/v2/everything?domains={}&apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
def news():
    '''
    Function that gets the json response to our url request
    '''
    get_base_url =base_url.format('bbc.co.uk')
    with urllib.request.urlopen(get_base_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        content = news_item.get('content')
        author = news_item.get('author')
        img = news_item.get('urlToImage')
        publishedAt= news_item.get('publishedAt')
        pub =  datetime.fromisoformat(publishedAt[:-1]).astimezone(timezone.utc)
        date = datetime.strftime(pub,"%x")  
        url = news_item.get('url')


        news_object = News(content,author,img,date, url)
        news_results.append(news_object)

    return news_results
def news_source():
    '''
    Function that gets the json response to our url request
    '''
   
    with urllib.request.urlopen(sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results