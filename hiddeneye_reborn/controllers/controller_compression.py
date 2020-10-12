from hiddeneye_reborn.models.model_compression import CompressionModel
import shutil
from os.path import exists
from os import makedirs


class CompressionController:
    def __init__(self, model=CompressionModel()):
        self._model = model
        self._compress_7zip = self._model.compress_7zip
        self._extract_7zip = self._model.extract_7zip

    def extract_7zip(self, filename, extract_dir=""):
        shutil.register_unpack_format('7zip', ['.7z'], self._extract_7zip)
        if extract_dir == "":
            if not exists("templates"):
                makedirs("templates")
            extract_dir = "templates"

        if ".7z" in filename:
            shutil.unpack_archive(filename=filename, extract_dir=extract_dir)
        else:
            raise ValueError("Invalid input, please add .7z to the end of your file and try again")

    def compress_7zip(self, archive_name, target_dir, go_to_dir=''):
        shutil.register_archive_format('7zip', self._compress_7zip, description='7zip archive')
        if go_to_dir == "":
            go_to_dir = "templates"
        if target_dir == "":
            raise ValueError("Target dir has to be specified")
        shutil.make_archive(archive_name, '7zip', go_to_dir, target_dir)

# TODO create templates_helper methods to get rid of default "templates" folders assignment
