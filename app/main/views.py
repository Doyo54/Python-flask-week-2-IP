from flask import render_template,request,redirect,url_for
from app import app
from ..request import news,news_source,search,specific_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    new = news()
    search_movie = request.args.get('name')

    if search_movie:
        return redirect(url_for('search_news',name=search_movie))
    else:
     return render_template('index.html', news = new)

@app.route('/alJazeera')
def alJazeera():

    '''
    View root page function that returns the source page and its data
    '''
    source = specific_source('al-jazeera-english')
    return render_template('alJazeera.html', source = source)

@app.route('/abc-news')
def abc():

    '''
    View root page function that returns the source page and its data
    '''
    source = specific_source('abc-news')
    return render_template('alJazeera.html', source = source)
@app.route('/espn')
def espn():

    '''
    View root page function that returns the source page and its data
    '''
    source = specific_source('espn')
    return render_template('espn.html', source = source)


@app.route('/sources')
def source():

    '''
    View root page function that returns the source page and its data
    '''
    source = news_source()
    return render_template('source.html', source = source)

@app.route('/search/<name>')
def search_news(name):
    title = f'search results for {name}'
    search_name_list = name.split(" ")
    search_name_format = "+".join(search_name_list)
    searched_news = search(search_name_format)
    return render_template('search.html',new = searched_news,title=title)


