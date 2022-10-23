import unittest
from app.tools.ChildParentLinksString import ChildParentLinksString
from app.binary_tree.BinaryTree import BinaryTree


class GeneralTest(unittest.TestCase):
    def test_multiple_invocation(self):
        bt = BinaryTree()
        for i in 22, 33, 11:
            bt.add(i, '')
        cpls = ChildParentLinksString(bt)
        self.assertEqual('1122 22 3322', cpls.get())
        bt.add(45, '')
        self.assertEqual('1122 22 3322 4533', cpls.get())
        bt.remove(11)
        self.assertEqual('2233 33 4533', cpls.get())

    def test_empty_tree(self):
        bt = BinaryTree()
        cpls = ChildParentLinksString(bt)
        self.assertEqual('', cpls.get())
