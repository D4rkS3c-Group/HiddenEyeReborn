from hiddeneye_reborn.models.model_connection import ConnectionModel
import urllib.request


class ConnectionController:

    """ConnectionController is used to verify, set and toggle connection.

    Todo:
        * Provide better summary to `__init__`
        * Improve documentation
        * Utilize setter and getter for host
    """
    def __init__(self, host, model=ConnectionModel()):
        """Utilizes `ConnectionModel()` if custom one not provided.

        Args:
            host (str): URL that will be used to verify connection. Defaults to `model.host` if not specified.

            model (Any): You don't want to specify this in most cases. Model that will be used as template and source of
            essential variables required by ConnectionController. Defaults to `ConnectionModel()` if not specified.
        """
        self._model = model
        self._host = host if not None else self._model.host

    def verify_connection(self):
        """Used to verify there is internet connection.

        Checking URL may be customized using `__init__`

        Returns:
            bool: The return value. True if connected (Status code 200), False otherwise.
        """
        return True if urllib.request.urlopen(url=self._host).getcode() == 200 else False
