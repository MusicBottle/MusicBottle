# -*- coding: utf-8 -*-
"""Unit tests for the WebServiceAPI class."""

from modules.WebServiceAPIs import WebServiceAPI
import unittest


class WebServiceAPIUnitTest(unittest.TestCase):
    """TestCase class for testing WebServiceAPI."""
    def setUp(self):
        self.wsapi = WebServiceAPI()

    def test_create_request_url(self):
        """Test WebServiceAPI.create_request_url()."""
        # The function currently only consists of "pass", so we're only
        # testing that it doesn't raise an exception.
        self.wsapi.create_request_url()

    def test_call(self):
        """Test WebServiceAPI.call()."""
        # Test "good" URLs
        good_urls = [
            'http://musicbrainz.org',
            'https://beta.musicbrainz.org/',
        ]
        for url in good_urls:
            result = self.wsapi.call(url)
            fail_message = 'Not an urlopen() returned object: {result}.'
            self.assertTrue(hasattr(result, 'geturl'),
                            fail_message.format(result=result)
                            )
        # Test that a bad URL fails
        self.assertRaises(ValueError, self.wsapi.call, 'spam')
