#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""MusicBrainz

MusicBrainz entity classes for MusicBottle.
"""
import json
from operator import itemgetter
from collections import *
from WebServiceAPIs import *

def date_to_tuple(date):
    date_length = len(date)
    if date_length == 4: #YYYY
        return (int(date),0,0)
    elif date_length == 7: #YYYY-MM
        return (int(date[:4]),int(date[5:7]),0)
    elif date_length == 10: #YYYY-MM-DD
        return (int(date[:4]),int(date[5:7]),int(date[8:10]))

    return None

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

        #Get nicely formated json string to print as debug
        self.data_string = json.dumps(self.data, sort_keys=True, indent=4)
        self.data_string = self.data_string.replace(" ", "&nbsp")
        self.data_string = self.data_string.replace("\n", "<br />")

        #First 100 release groups, categorized by secondary type.
        #Eg. compilation+remix = ...groups["+compilation+remix"]
        self.release_groups = defaultdict(list)
        #Number of release groups in each category
        self.release_group_counts = defaultdict(int)

        #TODO: Add support for multiple wikipedia pages
        #If there a multiple link languages, use user's preference.
        self.wikipedia = ("","") #Tuple format - text,domain
        for a in self.data['relations']:
            if a['type'] == "wikipedia":
                [domain,page_name]=a['url'].split("/wiki/")
                self.wikipedia = self.fetch_wikipedia(page_name,domain)["parse"]["text"]['*']
                summary_start = self.wikipedia.find("<p>")+3
                if summary_start != 2: #ie. was -1 before adding 3
                    summary_end = self.wikipedia.find("</p>")
                    self.wikipedia = (self.wikipedia[summary_start:summary_end],domain)
                break

        releases = self.fetch_releases(mbid, mb_server)

        for r in releases['release-groups']:
            t_str = ""
            for t in r['secondary-types']:
                t_str += "+"+t

            orig_date = date_to_tuple(r["first-release-date"])
            if orig_date is not None: #Don't display releases with no date.
                release_year = "" if orig_date[0] == 0 else str(orig_date[0])
                release_dict = {"data":r,\
                                "date":orig_date,\
                                "year":release_year}
                self.release_groups[t_str].append(release_dict)

        for key,value in self.release_groups.items():
            self.release_group_counts[key] = len(value)
            value.sort(key=itemgetter("date"))

    def fetch_data(self, mbid, mb_server):
        mb_api = MusicBrainzAPI('artist/'+mbid+'?inc=aliases+url-rels+releases&fmt=json',
                                mb_server)
        json_data = mb_api.response.read()
        return json.loads(json_data)

    def fetch_wikipedia(self, page_name, wp_server):
        wikipedia = WikipediaAPI('action=parse&prop=text&format=json&page='+page_name,wp_server)
        json_data = wikipedia.response.read();
        return json.loads(json_data)

    def fetch_releases(self, mbid, mb_server,offset=0):
        mb_api = MusicBrainzAPI('release-group?artist='+mbid+'&type=album&limit=100&offset='+str(offset)+'&fmt=json',mb_server)
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
