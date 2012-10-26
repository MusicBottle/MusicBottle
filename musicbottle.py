#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle

The MusicBottle website.
"""
import json

from modules.WebServiceAPIs import *
from modules.MusicBrainzEntities import *

# Debugging stuff
from platform import python_version_tuple
py_version = python_version_tuple()
if int(py_version[0]) < 3 and int(py_version[1]) < 7:
    from pprint import pformat as debug
else:
    from Pymo.pymo import pymo as debug

# Flask imports
from flask import Flask, request
from flaskext.babel import Babel

# Setup Flask
app = Flask(__name__)
# @TODO: Replace with proper configuration storage.
app.config['DEBUG'] = True
babel = Babel(app)

@app.route('/')
def musicbottle_welcome():
    return '<h1>Welcome to MusicBottle!</h1>'

@app.route('/artist/<artist_mbid>')
def musicbottle_artist(artist_mbid):
    artist = Artist(artist_mbid)
    response = artist.output()
    data = json.loads(response.read())
    debug_data = debug(data)
    return '<h1>'+data['name']+'</h1>'+debug_data

if __name__ == '__main__':
    app.run(port=19048)
