"""Touchwood tests."""
import unittest
from . import unittestsetup

import os
import sys

access_key = None
access_secret = None
api = None


class Test_Test(unittest.TestCase):
    """Tests."""

    def setUp(self):
        """setup for tests.

        provides an api instance
        """
        global access_key
        global access_secret
        global api

        try:
            access_key, access_secret = unittestsetup.auth()
        except Exception as e:
            sys.stderr.write("{}".format(e))
            exit(2)

    def test_import(self):
        """TEST: import."""
        import touchwood


if __name__ == "__main__":

    unittest.main()
