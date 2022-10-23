import unittest
from app.tools.TreeString import TreeString
from app.binary_tree.BinaryTree import BinaryTree


class GeneralTest(unittest.TestCase):
    def test_multiple_print(self):
        bt = BinaryTree()
        for i in 22, 33, 11:
            bt.add(i, '')
        ts = TreeString(bt)
        self.assertEqual('0110 112233 0330', ts.get())
        bt.add(45, '')
        self.assertEqual('0110 112233 03345 0450', ts.get())
        bt.remove(11)
        self.assertEqual('0220 223345 0450', ts.get())

    def test_empty_tree(self):
        bt = BinaryTree()
        ts = TreeString(bt)
        self.assertEqual('', ts.get())
