from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    groups = Group.get_groups()

    return render_template('index.html', title = title, groups=groups )

   

