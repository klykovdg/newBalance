import unittest
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.GetterSubtreeLens import GetterSubtreeLens


class GeneralTest(unittest.TestCase):
    def test_multiple_invocation(self):
        bt = BinaryTree()
        for i in 22, 33, 11:
            bt.add(i, '')
        gsl = GetterSubtreeLens(bt)
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        bt.add(45, '')
        self.assertEqual([[0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        bt.remove(11)
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_empty_tree(self):
        bt = BinaryTree()
        gsl = GetterSubtreeLens(bt)
        self.assertEqual([], gsl.get())
        bt.add(9, '')
        self.assertEqual([[0, 0]], gsl.get())
        bt.remove(9)
        self.assertEqual([], gsl.get())
