from flask import render_template
from app import app
from ..request import news,news_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    new = news()
    return render_template('index.html', news = new)

@app.route('/sources')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    source = news_source()
    return render_template('source.html', source = source)