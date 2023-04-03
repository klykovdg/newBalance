import unittest
from app.tools.TreeString import TreeString
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.GetterSubtreeLens import GetterSubtreeLens
from app.tools.ChildParentLinksString import ChildParentLinksString


class BinaryTreeGeneralTest(unittest.TestCase):
    def test_add_root(self):
        bt = BinaryTree()
        bt.add(5, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('050', ts.get())
        self.assertEqual([[0, 0]], gsl.get())
        self.assertEqual('5', cpls.get())

    def test_add_others(self):
        bt = BinaryTree()
        bt.add(7, '')
        bt.add(5, '')
        ts = TreeString(bt)
        self.assertEqual('050 570', ts.get())
        bt.add(9, '')
        self.assertEqual('050 579 090', ts.get())
        bt.add(1, '')
        bt.add(6, '')
        self.assertEqual('010 156 060 579 090', ts.get())
        bt.add(8, '')
        bt.add(10, '')
        self.assertEqual('010 156 060 579 080 8910 0100', ts.get())
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0,0]], gsl.get())
        self.assertEqual('15 57 65 7 89 97 109', cpls.get())

    def test_same(self):
        bt = BinaryTree()
        for i in 5, 6, 10, 3, 3, 3, 3, 6, 6, 8, 8, 10:
            bt.add(i, '')
        ts = TreeString(bt)
        self.assertEqual('030 350 5610 080 8100', ts.get())

    def test_zero(self):
        bt = BinaryTree()
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        bt.add(0, 'val')
        self.assertEqual('000', ts.get())
        self.assertEqual(bt.get(0), 'val')
        bt.remove(0)
        bt.add(7, '')
        bt.add(5, '')
        bt.add(8, '')
        bt.add(0, '')
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('000 050 578 080', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('05 57 7 87', cpls.get())

    def test_add_None(self):
        bt = BinaryTree()
        ts = TreeString(bt)
        bt.add(None, "None")
        self.assertEqual('', ts.get())
        bt.add(5, '')
        bt.add(1, '')
        bt.add(6, '')
        bt.add(None, '')
        self.assertEqual('010 156 060', ts.get())
