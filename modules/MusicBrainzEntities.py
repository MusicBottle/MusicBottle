#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBrainz

MusicBrainz entity classes for MusicBottle.
"""
import json
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
        self.data = self.fetch_data(mbid, mb_server)

    def fetch_data(self, mbid, mb_server):
        print mb_server
        mb_api = MusicBrainzAPI('artist/'+mbid+'?inc=aliases+url-rels&fmt=json',
                                mb_server)
        json_data = mb_api.response.read()
        return json.loads(json_data)
