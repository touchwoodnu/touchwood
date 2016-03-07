"""Exceptions."""

class TouchwoodAPIError(Exception):
    """Touchwood API error class - catches API response errors."""

    def __init__(self, error_response):
        """Instantiate a TouchwoodAPIError instance."""
        self.error_response = error_response
        msg = "Touchwood API returned error code %s (%s) " % \
              (error_response['code'], error_response['message'])

        super(TouchwoodAPIError, self).__init__(msg)
