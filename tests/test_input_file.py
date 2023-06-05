import unittest
import io
from main import *



class InputFileTest(unittest.TestCase):

    def test_file_not_null(self):
        self.assertNotEqual(readInput(), None)
        
    #check object is file
    def test_file_is_object(self):
        self.assertIsInstance(readInput(), io.TextIOBase, 'not a file')

