"""Touchwood tests."""
import unittest
from . import unittestsetup
import os
import sys
import json
import touchwood.api as touchwood

try:
    from nose_parameterized import parameterized, param
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

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

    @parameterized.expand([
                           (None,),
                           ("skantrae",),
                          ])
    def test__get_suppliers(self, supplier):
        """TEST: endpoint: touchwood/leveranciers."""
        r = None
        try:
            r = api.get_suppliers(supplier=supplier)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['leveranciers']) == 1)
            else:
                self.assertTrue(len(r['leveranciers']) > 1)

    @parameterized.expand([
                           ("skantrae",),
                          ])
    def test__get_assortments(self, supplier):
        """TEST: endpoint: touchwood/leveranciers/:supplier/assortimenten/."""
        r = None
        try:
            r = api.get_assortments(supplier=supplier)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['ass']) > 1)

    @parameterized.expand([
                           ("austria", "binnendeuren classicline", "VEERE"),
                          ])
    def test__get_properties(self, supplier, assortment, article):
        """TEST: endpoint: touchwood/leveranciers/:supplier/assortimenten/:assortment/:article/kenmerken/"""
        r = None
        try:
            r = api.get_properties(supplier=supplier, assortment=assortment,
                                   article=article)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['kenmerken']) > 1)

    @parameterized.expand([
                           ("austria", "binnendeuren classicline", "VEERE"),
                          ])
    def test__get_images(self, supplier, assortment, article):
        """TEST: endpoint: touchwood/leveranciers/:supplier/assortimenten/:assortment/:article/images/"""
        r = None
        try:
            r = api.get_images(supplier=supplier, assortment=assortment,
                               article=article)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['images']) == 3)

    @parameterized.expand([
                           ("austria", "binnendeuren classicline", "VEERE"),
                          ])
    def test__get_specs(self, supplier, assortment, article):
        """TEST: endpoint: touchwood/leveranciers/:supplier/assortimenten/:assortment/:article/specs/"""
        r = None
        try:
            r = api.get_specs(supplier=supplier, assortment=assortment,
                              article=article)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['ass']) > 1)

    @parameterized.expand([
                           ("austria", "binnendeuren classicline", "VEERE"),
                          ])
    def test__get_sizing(self, supplier, assortment, article):
        """TEST: endpoint: touchwood/leveranciers/:supplier/assortimenten/:assortment/:article/sizing/"""
        r = None
        try:
            r = api.get_sizing(supplier=supplier, assortment=assortment,
                               article=article)
        except touchwood.TouchwoodAPIError as e:
            print("{}".format(e))
        except Exception as e:
            print("{}".format(e))
        else:
            if supplier:
                self.assertTrue(len(r['mv']['sm']) == 2)

if __name__ == "__main__":

    unittest.main()
