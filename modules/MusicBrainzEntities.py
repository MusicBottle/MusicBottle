#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBrainz

MusicBrainz entity classes for MusicBottle.
"""
import json
import nltk
from WebServiceAPIs import *

class MusicBrainzEntity(object):
    """Parent class for all MusicBrainz entities."""
    def __init__(self, mbid):
        self.mbid = mbid

class Artist(MusicBrainzEntity):
    """"""
    def __init__(self, mbid, mb_server = 'http://musicbrainz.org'):
        self.mbid = mbid
        self.mb_server = mb_server
        self.data = self.fetch_data(mbid, self.mb_server)
        for a in self.data['relations']:
            if a['type'] == "wikipedia":
                if a['url'].find("en") > -1:
                    self.wikipedia = self.fetch_wikipedia(a['url'][a['url'].find("wiki/") + 5:],"http://en.wikipedia.org")
                    self.wikipedia = self.wikipedia['query']['pages'].values()[0]['revisions'][0]['*']
                    self.wikipedia = nltk.clean_html(self.wikipedia[self.wikipedia.find("<p>"):self.wikipedia.find("</p>")])
                    self.wikipedia = self.wikipedia.replace("&amp;", "&")
                    break
                
        self.releases = self.fetch_releases(mbid, self.mb_server)

    def fetch_data(self, mbid, mb_server):
        mb_api = MusicBrainzAPI('artist/'+mbid+'?inc=aliases+url-rels+releases&fmt=json',
                                mb_server)
        json_data = mb_api.response.read()
        return json.loads(json_data)
        
    def fetch_wikipedia(self, page_name, wp_server):
        wikipedia = WikipediaAPI('action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&rvparse=&rvsection=0&titles='+page_name,wp_server)
        json_data = wikipedia.response.read();
        return json.loads(json_data)
    
    def fetch_releases(self, mbid, mb_server):
        mb_api = MusicBrainzAPI('release?artist='+mbid+'&status=official&type=album&fmt=json',mb_server)
        json_data = mb_api.response.read()
        return json.loads(json_data)

class Release(MusicBrainzEntity):
    """"""
    def __init__(self, mbid, mb_server = 'http://musicbrainz.org'):
        self.mbid = mbid
        self.mb_server = mb_server
        self.data = self.fetch_data(mbid, mb_server)

    def fetch_data(self, mbid, mb_server):
        mb_api = MusicBrainzAPI('release/'+mbid+'?inc=artists+labels&fmt=json',
                                mb_server)
        json_data = mb_api.response.read()
        return json.loads(json_data)
