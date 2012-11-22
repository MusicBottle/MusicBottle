#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle WebServiceAPIs"""

import urllib2

class WebServiceAPI(object):
    """What do we want to know?
    - Is the site available via HTTP, HTTPS, something else?
    - What kind of data does it return (JSON, XML, ...)?
    - """
    def __init__(self): pass

    def create_request_url(self):
        """Placeholder function."""
        pass

    def call(self, url):
        return urllib2.urlopen(url)

class MediaWikiAPI(WebServiceAPI):
    """Parent class for MediaWiki based sites."""
    def __init__(self, request, server):
        self.server = server
        self.request = request
        self.request_url = server + '/w/api.php?' + request
        self.response = self.call(self.request_url)

class WikipediaAPI(MediaWikiAPI):
    pass

class FanartAPI(WebServiceAPI):
    """Class for getting information from fanart.tv."""
    def __init__(self, entity_type, mbid, apikey = None):
        if apikey is None:
            #@TODO: Print a log message saying FANART_APIKEY isn't set.
            self.response = None
        elif entity_type is not in ['Artist', 'Album', 'Label']:
            #@TODO: Log that the requested type doesn't exist.
            self.response = None
        else:
            try:
                from fanart.music import (entity_type)
                self.response = (entity_type).get(id = mbid)
            except ImportError:
                #@TODO: Print a log message saying the "fanart" module isn't
                #       available.
                self.response = None

class MusicBrainzAPI(WebServiceAPI):
    def __init__(self, request, server = 'http://musicbrainz.org'):
        self.server = server
        self.request = request
        self.request_url = server + '/ws/2/' + request
        self.response = self.call(self.request_url)
