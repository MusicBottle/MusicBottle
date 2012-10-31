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
    def __init__(self, mbid):
        self.mbid = mbid
        self.data = self.fetch_data(mbid)

    def fetch_data(self, mbid):
        mb_api = MusicBrainzAPI()
        json_data = mb_api.call('https://musicbrainz.org/ws/2/artist/'+mbid+
                                '?inc=aliases+url-rels&fmt=json').read()
        return json.loads(json_data)
