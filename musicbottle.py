#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle

The MusicBottle website.
"""
import urllib2
#import urlparse
import json
#import pymongo

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

class MusicBrainzEntity(object):
    """Parent class for all MusicBrainz entities."""
    def __init__(self, mbid):
        self.mbid = mbid

class Artist(MusicBrainzEntity):
    """"""

    def output(self):
        mb_api = MusicBrainzAPI()
        return mb_api.call('https://musicbrainz.org/ws/2/artist/'+self.mbid+'?inc=aliases&fmt=json')

class WebServiceAPI(object):
    """What do we want to know?
    - Is the site available via HTTP, HTTPS, something else?
    - What kind of data does it return (JSON, XML, ...)?
    - """
    def __init__(self): pass

    
    def create_request_url():
        """Placeholder function."""
        pass

    def call(self, url):
        return urllib2.urlopen(url)

class MediaWikiAPI(WebServiceAPI):
    """Parent class for MediaWiki based sites."""
    pass

class WikipediaAPI(MediaWikiAPI):
    pass

class MusicBrainzAPI(WebServiceAPI):
    pass

if __name__ == '__main__':
    app.run(port=19048)
