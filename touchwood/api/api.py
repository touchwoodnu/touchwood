"""Touchwood REST-API wrapper."""
import json
import requests
import six

APIVERSION = ""


class EndpointsMixin(object):
    """EndpointsMixin - API endpoints for the API class.

    each endpoint of the API has a representative method in EndpointsMixin
    Parameters that apply to the API url just need to be passed
    as a keyword argument.
    """

    def get_suppliers(self, supplier=None, **params):
        """get_suppliers - get a list of available suppliers.

        API-endpoints
        -------------
        touchwood/leveranciers
        touchwood/leveranciers/:leverancier

        returns :
            a dictionary containing a list of available suppliers or
            a list with only the details of the specified supplier
        """
        endpoint = "touchwood/leveranciers"

        if supplier:
            endpoint += "/{}".format(supplier)

        return self.request(endpoint, params=params)

    def get_assortments(self, supplier, **params):
        """get_assortments - get a list of available assortments.

        API-endpoints
        -------------
        touchwood/leveranciers/:leverancier/assortimenten
        touchwood/leveranciers/:leverancier/assortimenten/:assortiment

        returns :
            a dictionary containing a list of available assortments
        """
        endpoint = "touchwood/leveranciers/{}/assortimenten".format(supplier)

        return self.request(endpoint, params=params)

    def get_articles(self, supplier, assortment, **params):
        """get_articles - get all articles belonging to assortment.

        API-endpoints
        -------------
        touchwood/leveranciers/:supplier/assortimenten/:assortment/artikelen/

        returns :
            a dictionary containing a list of articles of the specified
            assortment
        """
        endpoint = "touchwood/leveranciers/{}/assortimenten/{}/artikelen".\
                   format(supplier, assortment)

        return self.request(endpoint, params=params)


class API(EndpointsMixin, object):
    """API - Touchwood API class for the Touchwood REST API."""

    def __init__(self, api_url, access_token=None, headers=None,
                 request_options=None):
        """Instantiate an instance of Touchwood API wrapper.

        Parameters
        ----------
        access_token : string (optional)
            Provide a valid access token if you have one.

        headers : dict (optional)
            Set HTTP-headers

        returns :
            a response dictionary
        """
        self.access_token = access_token
        self.request_options = request_options
        self.client = requests.Session()
        self.api_url = api_url

        # personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = 'Bearer '+self.access_token

        if headers:
            self.client.headers.update(headers)

    def request(self, endpoint, method='GET', params=None):
        """request - make an API request for the specified endpoint.

        this method is called by the EndpointMixin methods representing the
        endpoint. It is not called directly.

        Parameters
        ----------
        endpoint : string
            the API-endpoint

        method : string (optional)
            defaults to 'GET' and optionally another HTTP method representative
            for the API endpoint

        params : dict (optional)
            dictionary of parameters that apply to the Touchwood REST-API
            endpoint being called

        returns dict of response from Touchwood REST-API
        """
        if APIVERSION:
            endpoint = "{}/{}".format(APIVERSION, endpoint)
        url = "{}/{}".format(self.api_url, endpoint)

        # print("**** URL: {}".format(url))
        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)

        request_args = {}
        if self.request_options:
            for (k, v) in six.iteritems(self.request_options):
                request_args[k] = v

        if method == 'get':
            request_args['params'] = params
        else:
            request_args['data'] = params

        try:
            response = func(url, **request_args)
        except requests.RequestException as e:
            raise e
        content = response.content.decode('utf-8')

        content = json.loads(content)

        # error message
        if response.status_code >= 400:
            raise TouchwoodAPIError(content)

        return content
