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

class MusicBrainzAPI(WebServiceAPI):
    def __init__(self, request, server = 'http://musicbrainz.org'):
        self.server = server
        self.request = request
        self.request_url = server + '/ws/2/' + request
        self.response = self.call(self.request_url)
