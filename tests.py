#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""Test coverage for MusicBottle."""
import musicbottle
import unittest
from flask.ext.testing import TestCase

class MusicBottleTestCase(TestCase):

    def create_app(self):
        musicbottle.app.config['TESTING'] = True
        return musicbottle.app

    def test_index_page(self):
        rv = self.client.get('/')
        assert '<h1>Hello from The Bottle!</h1>' in rv.data

class CodeStyleTestCase(unittest.TestCase):
    """Tests that the code complies to coding style."""
    def setUp(self):
        self.files_to_check = self.find_files()

    def exclude_directory(self, directory):
        """Checks if a given directory should be excluded from the test."""
        # Exclude .hidden directories (e.g., .git, .tx).
        if directory[:1] == '.':
            return True
        # Exclude virtual environment directories.
        elif directory[-3:] == 'env':
            return True
        return False

    def include_file(self, filename):
        """Check if a given file should be included in the test."""
        # Only include Python files for now.
        if filename[-3:] == '.py':
            return True
        return False

    def find_files(self):
        import os
        py_files = []
        # Check if we're in the root of the project.
        if os.path.isfile('manage.py') and os.path.isdir('musicbottle'):
            for node in os.listdir(os.curdir):
                if os.path.isfile(node) and self.include_file(node):
                    py_files += [os.path.abspath(node)]
                elif os.path.isdir(node) and not self.exclude_directory(node):
                    for dirpath, dirnames, filenames in os.walk(node):
                        # Set dirpath to be absolute, to save the trouble later.
                        dirpath = os.path.abspath(dirpath)
                        for filename in filenames:
                            if self.include_file(filename):
                                py_files += [os.path.join(dirpath, filename)]
        else:
            #@TODO: Actually err out and stop the testcase somehow.
            print "We're not in the root of the project. Not running this test."
        return py_files

    def test_pep8_compliance(self):
        """Test that we comply with PEP 8."""
        import pep8
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(self.files_to_check)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

def main():
    """Main program. Run the tests."""
    import unittest
    unittest.main()

if __name__ == "__main__":
    main()
