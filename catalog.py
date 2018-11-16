from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    jsonify,
    make_response
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests


app = Flask(__name__)

app.secret_key = 'super_secret_key'
app.debug = True


# Index page
@app.route('/')
def showAll():
    state = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    title = "Welcome to Item Catalog Website"
    # categories = session.query(Category).all()
    # recentItems = session.query(CategoryItem).order_by(
    #                 CategoryItem.datetime.desc()).limit(10)
    return render_template(
                'index.html',
                title=title, STATE=state, login_session=login_session
                )
