# -*- coding: utf-8 -*-
"""Unit tests for the WebServiceAPI class."""

from modules.WebServiceAPIs import WebServiceAPI
import unittest


class WebServiceAPIUnitTest(unittest.TestCase):
    """TestCase class for testing WebServiceAPI."""
    def setUp(self):
        self.wsapi = WebServiceAPI()
        # Good URLs; format: [url, response attribute]
        self.urls = [
            ['http://musicbrainz.org', 'geturl'],
            ['https://beta.musicbrainz.org/', 'geturl'],
        ]
        # Bad URLs; format: [url, (exception(s) that should be raised)]
        self.urls_fail = [
            ['spam', (ValueError)],
        ]

    def test_create_request_url(self):
        """Test WebServiceAPI.create_request_url()."""
        try:
            # The function currently only consists of "pass", so...
            self.wsapi.create_request_url()
        except:
            self.fail('Calling create_request_url() resulted in an Exception.')

    def test_call(self):
        """Test WebServiceAPI.call()."""
        # Test "good" URLs
        for (url, attr) in self.urls:
            result = self.wsapi.call(url)
            self.assertTrue(hasattr(result, attr),
                            'Not an urlopen() returned object: {url}.'.format(
                                url=url,
                            ))
        # Test "bad" URLs
        for (url, exception) in self.urls_fail:
            print url, exception
            self.assertRaises(exception, self.wsapi.call, url)
