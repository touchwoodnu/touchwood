"""CartEndpoints."""


class CartEndpointsMixin(object):
    """CartEndpointsMixin - API endpoints covering cart functionality.

    each endpoint of the API has a representative method in CartEndpointsMixin.
    Parameters that apply to the API url need to be passed as keyword argument.

    cart/items/                 GET     list all items in cart
    cart/items/:cid/            GET     list specific item in cart

    cart/items                  POST    add an item to the cart
                                        body: { "id" : <article-id>,
                                                "csrfmiddlewaretoken" : <tok> }
    cart/items                  DELETE  delete all items
    cart/items/:cid/            DELETE  delete item with cart-id cid
    """

    def cart_get_items(self, **params):
        """cart_get_items - get a list of stored cart items.

        API-endpoint
        -------------
        cart/items

        returns :
            a dictionary containing article information of all items.
        """
        endpoint = "cart/items"

        return self.request(endpoint, params=params)

    def cart_get_item(self, cid, **params):
        """cart_get_item - get a specific item from cart.

        API-endpoint
        -------------
        cart/item

        lookup the specified item in the cart by it's cart-id (cid) and return
        it's related information.

        If cid is not specified a ValueError is raised.

        returns :
            a dictionary containing article information of the specified item.
        """
        endpoint = "cart/items"
        if not cid:
            raise ValueError("cid = " + str(cid))

        endpoint += "/{}".format(cid)

        return self.request(endpoint, params=params)

    def cart_add_item(self, **params):
        """cart_add_item - add item to cart.

        API-endpoint
        -------------
        cart/items

        add an item to the cart. This is done by passing the id of the article
        in a JSON formatted body to the server:

            {
              "id" : "N901",
              "csrfmiddlewaretoken" : "Yy5qSxbT4eAJnFnQbUR3nh75rDN4Riwm"
            }

        The server queries it's resources for the article and adds it to the
        cart.

        returns :
            a dictionary containing cart-id (cid) for the new article:

            {
               "cid": <cid>
            }

        """
        endpoint = "cart/items"

        return self.request(endpoint, "POST", params=params)

    def cart_delete_item(self, item=None, **params):
        """cart_delete_item - delete item from cart.

        API-endpoints
        -------------
        cart/items

        returns :
            in case the item is specified with a cid,
            a dictionary containing cart-id (cid) for the article to delete:

              {
                "cid": <cid>
              }

            HTTP status 200 if success
            HTTP status 404 if not found

            in case there is no item specified, all items will be deleted
            and a dictionary:

              {
                "deleted": <num>
              }

            is returned. In the latter case always with return HTTP status 200.
        """
        endpoint = "cart/items"
        if item:
            endpoint += "/{}".format(item)

        return self.request(endpoint, "DELETE", params=params)
