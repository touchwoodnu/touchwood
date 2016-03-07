"""Touchwood tests."""
import unittest
from . import unittestsetup
import os
import sys
import json
import touchwood.api as touchwood

access_key = None
access_secret = None
apiserver = None
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
        global apiserver

        try:
            access_key, access_secret = unittestsetup.auth()
        except Exception as e:
            sys.stderr.write("{}".format(e))
            exit(2)
        else:
            apiserver = os.getenv("TW_API_SERVER")
            api = touchwood.API(apiserver, request_options={"verify": False})

    def test_leveranciers(self):
        """TEST: endpoint: touchwood/leveranciers."""
        r = None
        try:
            r = api.get_suppliers()
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            self.assertTrue(len(r['leveranciers']))

if __name__ == "__main__":

    unittest.main()
