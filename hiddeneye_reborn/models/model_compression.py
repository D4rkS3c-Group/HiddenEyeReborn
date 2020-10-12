import py7zr


class CompressionModel:
    def __init__(self, model_7zip = py7zr):
        self._model_7zip = model_7zip
        self._compress_7zip = self._model_7zip.pack_7zarchive
        self._extract_7zip = self._model_7zip.unpack_7zarchive

    @property
    def model_7zip(self):
        return self._model_7zip

    @model_7zip.setter
    def model_7zip(self, new_7zip_model):
        self._model_7zip = new_7zip_model

    @property
    def compress_7zip(self):
        return self._compress_7zip

    @compress_7zip.setter
    def compress_7zip(self, new_7zip_compressor):
        self._compress_7zip = new_7zip_compressor

    @property
    def extract_7zip(self):
        return self._extract_7zip

    @extract_7zip.setter
    def extract_7zip(self, new_7zip_extractor):
        self._extract_7zip = new_7zip_extractor
