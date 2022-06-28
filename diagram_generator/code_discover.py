import os
import re
# data types
from typing import List


class CodeDiscover:
    def __init__(self, root_directory: str) -> None:
        self.file_graph: dict = {}
        self.root_directory: str = root_directory
        self.FILES_KEY: str = "files"
        self.DIRECORIES_KEY: str = "directories"
        self.MODULE_DEF: str = "__init__.py"
        self.module_def_refEx: re = re.compile("__init__.py$")
        self.python_file_regEx: re = re.compile(".py$")

    def is_module(self, directory: str):
        directories = os.listdir(directory)
        for _directory in directories:
            # TODO: Change this to regex
            if self.module_def_refEx.search(_directory):
                return True
        return False

    def get_python_code(self, directory: str):
        files = []
        _ = self.get_directory_files_and_folders(directory)
        _files = _[self.FILES_KEY]
        for _inner_file in _files:
            if self.python_file_regEx.search(_inner_file):
                files.append(_inner_file)
        _directories = _[self.DIRECORIES_KEY]
        if _directories:
            for directory in _directories:
                if self.is_module(directory):
                    files = _files + self.get_python_code(directory)
        return files

    def get_directory_files_and_folders(self, directory: str):
        _directories = os.listdir(directory)
        files = []
        directories = []
        for directory in _directories:
            current_path = "{root}/{directory}".format(
                root=self.root_directory,
                directory=directory
            )
            if os.path.isdir(current_path):
                directories.append(current_path)
            else:
                files.append(current_path)
        return {self.FILES_KEY: files,   self.DIRECORIES_KEY: directories}
