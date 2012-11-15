#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle

The MusicBottle website.
"""

# Flask imports
from flask import Flask, request, render_template

# MusicBottle imports
from modules.MusicBrainzEntities import *

# Debugging stuff
from platform import python_version_tuple
py_version = python_version_tuple()

if int(py_version[0]) < 3 and int(py_version[1]) < 7:
    from pprint import pformat as debug
else:
    from Pymo.pymo import pymo as debug

# Setup Flask
app = Flask(__name__)
# @TODO: Replace with proper configuration storage.
# @TODO: Add configuration for MusicBrainz server to query
# @TODO: Add configuration for fanart.tv API key
app.config['DEBUG'] = True

@app.route('/')
def musicbottle_welcome():
    return render_template('index.html')

@app.route('/artist/<artist_mbid>')
def musicbottle_artist(artist_mbid):
    artist = Artist(artist_mbid)
    debug_data = debug(artist.data)
    return render_template('artist.html', artist=artist)

