import urllib.request,json
from .models import News,Source
import datetime
from datetime import datetime, timezone

base_url = 'https://newsapi.org/v2/everything?domains={}&apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
search_url = 'https://newsapi.org/v2/everything?q={}&apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
def news():
    '''
    Function that gets the json response to our url request
    '''
    get_base_url =base_url.format('aljazeera.com,bbc.co.uk,us.cnn.com,techcrunch.com,engadget.com')
    with urllib.request.urlopen(get_base_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)


    return news_results
def process_news(news_list):
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
            news_results = process_source(news_results_list)


    return news_results

def process_source(news_list):
    '''
    Function  that processes the news sources result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description =news_item.get('description')
        country = news_item.get('country')
        url = news_item.get('url')


        news_object = Source(name,description,country, url)
        news_results.append(news_object)

    return news_results
def search(name):
    '''
    Function that gets the json response to our url request
    '''
    searched = search_url.format(name)
    with urllib.request.urlopen(searched) as url:
       search_news_data = url.read()
       search_news_response = json.loads(search_news_data)

       search_news_results = None

       if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_news(search_news_list)


    return search_news_results    