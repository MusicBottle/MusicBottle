#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""Test coverage for MusicBottle.


"""
import os
import musicbottle
from flask.ext.testing import TestCase

class MusicBottleTestCase(TestCase):

    def create_app(self):
        musicbottle.app.config['TESTING'] = True
        return musicbottle.app

    def test_index_page(self):
        rv = self.client.get('/')
        assert '<h1>Hello from The Bottle!</h1>' in rv.data

def main():
    """Main program. Run the tests."""
    import unittest
    unittest.main()

if __name__ == "__main__":
    main()
