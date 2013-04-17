#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle

The MusicBottle website.
"""

# Regular Python imports
from os import getenv
import urllib

# Using simplejson (faster) if available otherwise using stdlib json.
try:
    import simplejson as json
except ImportError:
    import json

# Flask imports
from flask import Flask, request, render_template
from flask.ext.babel import Babel

# MusicBottle imports
from modules.MusicBrainzEntities import *

# Setup Flask
app = Flask(__name__)
app.config.from_object('musicbottle.default_settings')
if getenv('MUSICBOTTLE_SETTINGS') is not None:
    app.config.from_envvar('MUSICBOTTLE_SETTINGS')
babel = Babel(app)
# Adding expression statements to jinja2 templates
app.jinja_env.add_extension('jinja2.ext.do')


@babel.localeselector
def get_locale():
    # List which languages we support.
    #@TODO: Automatically detect this somehow.
    supported_languages = ['da', 'en', 'nb']
    # Use the browser's settings to determine which language to serve.
    #@TODO: Enable setting a cookie or something instead.
    return request.accept_languages.best_match(supported_languages)


@app.route('/', endpoint='home')
def musicbottle_welcome():
    return render_template('index.html')


@app.route('/artist/<artist_mbid>', endpoint='artist')
def musicbottle_artist(artist_mbid):
    artist = Artist(artist_mbid, app.config['MUSICBRAINZ_SERVER'], apikeys={
        'fanart.tv': app.config['FANART_APIKEY'],
    })
    return render_template('artist.html', artist=artist)


@app.route('/artist/<artist_mbid>/discography', endpoint='discography')
def musicbottle_artist_discography(artist_mbid):
    artist = Artist(artist_mbid, app.config['MUSICBRAINZ_SERVER'])
    return render_template('discography.html', artist=artist)


@app.route('/release/<release_mbid>')
def musicbottle_release(release_mbid):
    release = Release(release_mbid, app.config['MUSICBRAINZ_SERVER'])
    return render_template('release.html', release=release)


@app.route('/search/')
def musicbottle_search():
    type = request.args.get('type', 'artist')
    query = request.args.get('query')
    if type and query:
        # NOTE: I was getting <UnicodeDecodeError> from MusicBrainzAPI().
        # response().read() thats why added .decode("utf-8", "replace"))
        params = {'fmt': 'json', 'query': query}
        results = json.loads(MusicBrainzAPI('%s?%s' % (type, urllib.
                             urlencode(params))).response.read().
                             decode("utf-8", "replace"))
        results['type'] = type
    else:
        results = {}
    return render_template('search.html', results=results)


@app.context_processor
def utility_processor():
    from flask import Markup
    return dict(Markup=Markup)
