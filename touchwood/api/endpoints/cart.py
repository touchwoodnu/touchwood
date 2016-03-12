"""CartEndpoints."""


class CartEndpointsMixin(object):
    """CartEndpointsMixin - API endpoints covering cart functionality.

    each endpoint of the API has a representative method in CartEndpointsMixin.
    Parameters that apply to the API url need to be passed as keyword argument.

    cart/items/                 GET     list all items in cart
    cart/items/:id/             GET     list specific item in cart

    cart/items                  POST    add an item to the cart
                                        body: { "id" : <article-id>,
                                                "csrfmiddlewaretoken" : <tok> }
    """

    def cart_get_items(self, **params):
        """cart_get_items - get a list of stored cart items.

        API-endpoints
        -------------
        cart/items

        returns :
            a dictionary containing article information of all items
        """
        endpoint = "cart/items"

        return self.request(endpoint, params=params)

    def cart_get_item(self, item, **params):
        """cart_get_item - get a specific item from cart.

        API-endpoints
        -------------
        cart/item

        returns :
            a dictionary containing article information
        """
        endpoint = "cart/item"
        if not item:
            raise ValueError("item = " + str(item))

        endpoint += "{}/".format(item)

        return self.request(endpoint, params=params)

    def cart_add_item(self, item, **params):
        """cart_add_item - add item to cart.

        API-endpoints
        -------------
        cart/items

        returns :
            a dictionary containing cart-id (cid) for the new article
        """
        endpoint = "cart/item"
        if not item:
            raise ValueError("item = " + str(item))

        endpoint += "{}/".format(item)

        return self.request(endpoint, "POST", params=params)
