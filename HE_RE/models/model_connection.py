class ConnectionModel:

    """Provides default values for `ConnectionController()`"""
    def __init__(self, host: str = "https://google.com"):

        """
        Args:
            host: Default URL for connection checking needs.
        """
        self._host = host

    @property
    def host(self):
        """
        Returns:
            str: returns value of host.
        """
        return self._host

    @host.setter
    def host(self, new_host: str):
        """
        Args:
            new_host: New URL to set as host.
        """
        self._host = new_host
