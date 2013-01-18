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

    def verify_wsapi_call(self, url):
        result = self.wsapi.call(url)

        msg = 'Not an urlopen() returned object: %s.' % (result)
        self.assertTrue(hasattr(result, 'geturl'), msg)

    def test_call(self):
        """Test WebServiceAPI.call()."""

        # Test "good" URLs
        self.verify_wsapi_call('http://musicbrainz.org')
        self.verify_wsapi_call('https://beta.musicbrainz.org/')

        # Test that a bad URL fails
        self.assertRaises(ValueError, self.wsapi.call, 'spam')
