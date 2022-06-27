import os
# data types
from typing import List


class CodeDiscover:
    def __init__(self):
        self.file_graph: dict = {}
        self.root_directory: str = None

    def set_root_directory(self) -> None:
        pass

    def get_directories(self, path: List[str]):
        pass

    def get_python_files(self):
        pass

    def is_python_module(self):
        pass

    def add_file_node(self, file: str):
        pass
