import unittest
import os

from diagram_generator.code_discover import CodeDiscover


class TestCodeDiscover(unittest.TestCase):

    def setUp(self):
        self.default_module: str = os.getcwd()+'/diagram_generator/' 
        self.empty_directory: str = self.default_module + '/test/NONE/'
        self.sample_directory: str = self.default_module + "/test/samples/"

    def test_is_module(self):
        code_discover = CodeDiscover(self.default_module)
        self.assertTrue(
            code_discover.is_module(self.default_module)
        )
        self.assertTrue(
            code_discover.is_module(self.sample_directory)
        )
        self.assertFalse(
            code_discover.is_module(self.empty_directory)
        )

    def get_python_code(self):
        code_discover = CodeDiscover(self.default_module)
        python_files = code_discover(self.sample_directory)
        self.assertIn(
            self.sample_directory+"sample_1.py",
            python_files
        )
        self.assertIn(
            self.sample_directory+"sample_2.py",
            python_files
        )
        python_files = code_discover(self.empty_directory)
        self.assertNotIn(
            self.sample_directory+"sample_1.py",
            python_files
        )
        self.asserNotIn(
            self.sample_directory+"sample_2.py",
            python_files
        )
        self.assertEqual(
            [],
            python_files
        )
