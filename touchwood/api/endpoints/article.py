"""Touchwood REST-API wrapper."""

APIVERSION = ""


class ArticleEndpointsMixin(object):
    """ArticleEndpointsMixin - API endpoints for the API class.

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

    def get_properties(self, supplier, assortment, article, **params):
        """get_properties - get properties of specified article.

        API-endpoints
        -------------
        touchwood/leveranciers/:supplier/assortimenten/:assortment/artikelen/:artikel/kenmerken/

        returns :
            a dictionary containing a list of properties of the specified
            article
        """
        endpoint = ("touchwood/leveranciers/{}/assortimenten/{}/" +
                    "artikelen/{}/kenmerken").format(supplier,
                                                     assortment,
                                                     article)

        return self.request(endpoint, params=params)

    def get_images(self, supplier, assortment, article, **params):
        """get_images - get images of specified article.

        API-endpoints
        -------------
        touchwood/leveranciers/:supplier/assortimenten/:assortment/artikelen/:artikel/images/

        returns :
            a dictionary containing a list of images of the specified
            article
        """
        endpoint = ("touchwood/leveranciers/{}/assortimenten/{}/" +
                    "artikelen/{}/images").format(supplier,
                                                  assortment,
                                                  article)

        return self.request(endpoint, params=params)

    def get_specs(self, supplier, assortment, article, **params):
        """get_specs - get specs of specified article.

        API-endpoints
        -------------
        touchwood/leveranciers/:supplier/assortimenten/:assortment/artikelen/:artikel/specs/

        returns :
            a dictionary containing a list of configuration specs of the
            specified article
        """
        endpoint = ("touchwood/leveranciers/{}/assortimenten/{}/" +
                    "artikelen/{}/specs").format(supplier,
                                                 assortment,
                                                 article)

        return self.request(endpoint, params=params)

    def get_sizing(self, supplier, assortment, article, **params):
        """get_sizing - get sizing options of specified article.

        API-endpoints
        -------------
        touchwood/leveranciers/:supplier/assortimenten/:assortment/artikelen/:artikel/maatvoering/

        returns :
            a dictionary containing a sizing specs of the specified article.
        """
        endpoint = ("touchwood/leveranciers/{}/assortimenten/{}/" +
                    "artikelen/{}/maatvoering").format(supplier,
                                                       assortment,
                                                       article)

        return self.request(endpoint, params=params)
