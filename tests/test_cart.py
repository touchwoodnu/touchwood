"""Touchwood API cart tests."""
import unittest
from . import unittestsetup
import os
import sys
import json
import touchwood.api as touchwood
from requests.utils import dict_from_cookiejar, cookiejar_from_dict

try:
    from nose_parameterized import parameterized, param
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_key = None
access_secret = None
apiserver = None
api = None

csrfmiddlewaretoken = "sQ9LJGWxr2mBw0nDdmFn"


class Test_CartAPI(unittest.TestCase):
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

        # make sure we have a session
        sessionid = os.getenv("TW_SESSION_ID")
        if not sessionid:
            # get one
            # perform a request to get a session cookie
            # and clear the cart
            r = api.cart_delete_item()
            jar = dict_from_cookiejar(api.client.cookies)

            # save it
            sessionid = jar['sessionid']
            # put it on the environment for reuse
            os.environ["TW_SESSION_ID"] = sessionid

        # restore the sessionid cookie
        api.client.cookies = cookiejar_from_dict(dict(sessionid=sessionid))

    @parameterized.expand([(["N900"], None),
                           (["N900", "N901", "VEERE"], []),
                           (["N900", "N901", "VEERE"], ["N901"])
                           ])
    def test__cart_delete_item(self, articles, todelete):
        """cart_delete_item."""
        self.added = {}
        # first we add items
        for A in articles:
            toadd = dict(id=A, csrfmiddlewaretoken=csrfmiddlewaretoken)
            r = api.cart_add_item(**toadd)
            # save this addition as : articleId : cid in the added dict
            self.added.update({A: r['cid']})

        if not todelete:
            # nothing specific to delete: delete all
            # what do we have ?
            r = api.cart_get_items()
            cnt = len(r['items'])

            r = api.cart_delete_item()
            self.assertTrue(r['deleted'] == cnt)
        else:
            r = api.cart_get_items()
            cntBefore = len(r['items'])
            for A in todelete:
                cid = self.added[A]
                r = api.cart_delete_item(item=cid)
                self.assertTrue(r['cid'] == cid)

            # determine #items after deleting specific items
            r = api.cart_get_items()
            cntAfter = len(r['items'])
            self.assertTrue(cntBefore == cntAfter + len(todelete))

    @parameterized.expand([(["N900"],),
                           (["N900", "N901", "VEERE"],),
                           (["N900", "N901", "VEERE"],)
                           ])
    def test__add_item(self, articles):
        """cart_add_item and cat_get_item."""
        # make sure cart is empty
        r = api.cart_delete_item()
        r = api.cart_get_items()
        self.assertTrue(r['items'] == {})

        for A in articles:
            toadd = dict(id=A, csrfmiddlewaretoken=csrfmiddlewaretoken)
            r = api.cart_add_item(**toadd)
            # save this addition as : articleId : cid in the added dict
            justAdded = r['cid']
            # get it from the cart
            r = api.cart_get_item(cid=justAdded)
            self.assertTrue(justAdded in r['items'] and
                            A == r['items'][justAdded]['article']['id'])

    @parameterized.expand([(["N900"], "2", "10.0"),
                           (["N901"], "5", None),
                           (["N902"], None, "15.0"),
                           ])
    def test__update_item(self, articles, count, rebate):
        """cart_update_item."""
        # make sure cart is empty
        r = api.cart_delete_item()
        r = api.cart_get_items()
        self.assertTrue(r['items'] == {})

        for A in articles:
            toadd = dict(id=A, csrfmiddlewaretoken=csrfmiddlewaretoken)
            r = api.cart_add_item(**toadd)
            justAdded = r['cid']
            # get it from the cart
            r = api.cart_get_item(cid=justAdded)
            self.assertTrue(justAdded in r['items'] and
                            A == r['items'][justAdded]['article']['id'])
            # update
            toupd = dict()
            if count:
                toupd.update({'aantal': count})
            if rebate:
                toupd.update({'korting': rebate})

            # make the request to update the named parameters
            r = api.cart_update_item(cid=justAdded, **toupd)

            self.assertTrue(
                justAdded == r['cid'] and
                (not rebate or float(rebate) == float(r['korting'])) and
                (not count or count == r['aantal']))


if __name__ == "__main__":

    unittest.main()
