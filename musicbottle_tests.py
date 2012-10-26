#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""Test coverage for MusicBottle.


"""
import os
import musicbottle
import unittest

class MusicBottleTestCase(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_index_page(self):
        rv = self.app.get('/')
        assert '<h1>Welcome to MusicBottle!</h1>' in rv.data

if __name__ == "__main__":
    unittest.main()
