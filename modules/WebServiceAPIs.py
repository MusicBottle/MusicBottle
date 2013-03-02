#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBottle WebServiceAPIs"""

import urllib2


class WebServiceAPI(object):
    """What do we want to know?
    - Is the site available via HTTP, HTTPS, something else?
    - What kind of data does it return (JSON, XML, ...)?
    - """
    def __init__(self, url):
        self.url = url
        self.response = self.call(url)

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
    """Class for getting information from fanart.tv.

    Mapping is Artist-Artist, Label-Label, Album-Release Group.

    Information about type, sort, and limit can be found in the API:
    http://fanart.tv/api-docs/music-api/
    """
    def __init__(self, entity_type, mbid, apikey=None,
                 type="all", sort=1, limit=2):
        self.supported_entity_types = ('artist', 'album', 'label')
        self._request_url_base = 'http://api.fanart.tv/webservice/' + \
                                 '{entity_type}/{key}/{mbid}/' + \
                                 'json/{type}/{sort}/{limit}/'
        self._entity_type = entity_type.lower()
        if apikey is None:
            #@TODO: Print a log message saying FANART_APIKEY isn't set.
            self.response = None
        elif self._entity_type not in self.supported_entity_types:
            #@TODO: Log that the requested type doesn't exist.
            self.response = None
        else:
            self._request_url = self._request_url_base.format(**{
                'entity_type': self._entity_type,
                'key': apikey,
                'mbid': mbid,
                'type': type,
                'sort': sort,
                'limit': limit,
            })
            self.response = self.call(self._request_url)
            #@TODO: Catch and log if something goes awry with the HTTP request.


class MusicBrainzAPI(WebServiceAPI):
    def __init__(self, request, server='http://musicbrainz.org'):
        self.server = server
        self.request = request
        self.request_url = server + '/ws/2/' + request
        self.response = self.call(self.request_url)
