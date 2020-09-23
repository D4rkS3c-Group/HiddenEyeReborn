class ConnectionModel:
    def __init__(self, host: str = "https://google.com"):
        self._host = host

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, new_host: str):
        self._host = new_host
