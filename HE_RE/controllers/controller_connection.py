from HE_RE.models.model_connection import ConnectionModel
import urllib.request


class ConnectionController:
    def __init__(self, model=ConnectionModel()):
        self._model = model
        self._host = model.host

    def verify_connection(self):
        return True if urllib.request.urlopen(url=self._host).getcode() == 200 else False
