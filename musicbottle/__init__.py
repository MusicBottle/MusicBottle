#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle

The MusicBottle website.
"""

# Regular Python imports
from os import getenv

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
app.config.from_object('musicbottle.default_settings')
if getenv('MUSICBOTTLE_SETTINGS') is not None:
    app.config.from_envvar('MUSICBOTTLE_SETTINGS')

@app.route('/')
def musicbottle_welcome():
    return render_template('index.html')

@app.route('/artist/<artist_mbid>')
def musicbottle_artist(artist_mbid):
    artist = Artist(artist_mbid, app.config['MUSICBRAINZ_SERVER'])
    debug_data = debug(artist.data)
    return render_template('artist.html', artist=artist)
