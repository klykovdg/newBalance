import unittest
from app.tools.GetterSubtreeLens import GetterSubtreeLens
from app.tools.TreeString import TreeString
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.ChildParentLinksString import ChildParentLinksString


class BinaryTreeGRRTest(unittest.TestCase):
    def test_grr_add1(self):
        bt = BinaryTree()
        for i in 7, 5, 9, 2, 3:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 235 050 379 090', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('23 37 53 7 97', cpls.get())

    def test_grr_add2(self):
        bt = BinaryTree()
        for i in 10, 5, 12, 2, 7, 16, 1, 4, 3:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 123 030 245 057 070 41012 01216 0160', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 24 32 410 54 75 10 1210 1612', cpls.get())

    def test_grr_add3(self):
        bt = BinaryTree()
        for i in 10, 5, 12, 2, 7, 16, 1, 3, 4:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 120 235 040 457 070 31012 01216 0160', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 23 310 45 53 75 10 1210 1612', cpls.get())

    def test_grr_add4(self):
        bt = BinaryTree()
        for i in 7, 3, 5:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('030 357 070', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('35 5 75', cpls.get())

    def test_grr_add5(self):
        bt = BinaryTree()
        for i in 10, 5, 12, 1, 6, 8:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 150 5610 080 81012 0120', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('15 56 6 810 106 1210', cpls.get())

    def test_grr_add6(self):
        bt = BinaryTree()
        for i in 10, 5, 12, 1, 7, 6:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 156 060 5710 01012 0120', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('15 57 65 7 107 1210', cpls.get())

    def test_grr_remove1(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 45, 60, 10, 25, 37, 70, 27:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('37', bt.remove(37))
        self.assertEqual('0100 10200 202530 0270 273035 0350 254050 0450 455060 06070 0700', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0],
                          [3, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 2025 2540 2730 3025 3530 40 4550 5040 6050 7060', cpls.get())

    def test_grr_remove2(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 45, 60, 10, 25, 31, 70, 27:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('30', bt.remove(30))
        self.assertEqual('0100 10200 202531 0270 273135 0350 254050 0450 455060 06070 0700', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0],
                          [3, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 2025 2540 2731 3125 3531 40 4550 5040 6050 7060', cpls.get())
