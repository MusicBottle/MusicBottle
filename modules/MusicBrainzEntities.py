#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBrainz

MusicBrainz entity classes for MusicBottle.
"""

class MusicBrainzEntity(object):
    """Parent class for all MusicBrainz entities."""
    def __init__(self, mbid):
        self.mbid = mbid

class Artist(MusicBrainzEntity):
    """"""

    def output(self):
        mb_api = MusicBrainzAPI()
        return mb_api.call('https://musicbrainz.org/ws/2/artist/'+self.mbid+'?inc=aliases+u&fmt=json')
