import unittest
import os, glob, sys
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.pgprint import pgprint
from io import StringIO


RESOURCES = '../../resources/pgprint'
ELEM = 'elements.txt'
MODEL = 'prettyprint.txt'


class PGPrint(unittest.TestCase):

    def test(self):
        path = os.path.abspath(RESOURCES)
        l = sorted(glob.glob(path + os.sep + "*"))
        for i in l:
            bt = BinaryTree()
            value = ''
            file_elems_path = i + os.sep + ELEM
            file_model_path = i + os.sep + MODEL
            for key in open(file_elems_path):
                bt.add(int(key.strip()), value)
            expected_tree = open(file_model_path).read().rstrip()

            buff = StringIO()
            temp = sys.stdout
            sys.stdout = buff
            pgprint(bt)
            actual_tree = buff.getvalue().rstrip()
            sys.stdout = temp

            self.assertEqual(expected_tree, actual_tree, i)
