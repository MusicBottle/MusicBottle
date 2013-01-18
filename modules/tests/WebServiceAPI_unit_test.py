# -*- coding: utf-8 -*-
"""Unit tests for the WebServiceAPI class."""

from modules.WebServiceAPIs import WebServiceAPI
import unittest


class WebServiceAPIUnitTest(unittest.TestCase):
    """TestCase class for testing WebServiceAPI."""
    def setUp(self):
        self.wsapi = WebServiceAPI()
        self.urls = [
            ['http://musicbrainz.org', 'geturl'],
            ['https://beta.musicbrainz.org/', 'geturl'],
        ]
        self.urls_fail = [
            ['spam', (ValueError)],
        ]

    def test_create_request_url(self):
        try:
            self.wsapi.create_request_url()
        except:
            self.fail('Calling create_request_url() resulted in an Exception.')

    def test_call(self):
        for (url, attr) in self.urls:
            result = self.wsapi.call(url)
            self.assertTrue(hasattr(result, attr),
                            'Not an urlopen() returned object: {url}.'.format(
                                url=url,
                            ))
        for (url, exception) in self.urls_fail:
            print url, exception
            self.assertRaises(exception, self.wsapi.call, url)
