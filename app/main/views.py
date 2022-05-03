from flask import render_template
from app import app
from ..request import news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    new = news()
    return render_template('index.html', news = new)