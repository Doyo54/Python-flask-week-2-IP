import urllib.request,json
from .models import News

base_url = 'https://newsapi.org/v2/everything?q=Apple&from=2022-05-03&sortBy=popularity&apiKey=f571903dfdd44dc9b15e9e68d3cc9e88'
def news():
    '''
    Function that gets the json response to our url request
    '''
   
    with urllib.request.urlopen(base_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        content = news_item.get('content')
        author = news_item.get('author')

        news_object = News(content,author)
        news_results.append(news_object)

    return news_results
