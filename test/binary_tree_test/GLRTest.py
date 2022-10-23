import unittest
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.TreeString import TreeString
from app.tools.GetterSubtreeLens import GetterSubtreeLens
from app.tools.ChildParentLinksString import ChildParentLinksString


class BinaryTreeGLRTest(unittest.TestCase):
    def test_glr_add1(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 10:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 4710 090 91012 0120', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('47 7 910 107 1210', cpls.get())

    def test_glr_add2(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 8, 2, 10, 15, 11:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 240 4710 080 890 91012 0110 111215 0150', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('24 47 7 89 910 107 1112 1210 1512', cpls.get())

    def test_glr_add3(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 13, 8, 2, 12, 15, 11:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 240 4712 080 8911 0110 91213 01315 0150', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('24 47 7 89 912 119 127 1312 1513', cpls.get())

    def test_glr_add4(self):
        bt = BinaryTree()
        for i in 7, 9, 8:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('070 789 090', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('78 8 98', cpls.get())

    def test_glr_add5(self):
        bt = BinaryTree()
        for i in 7, 4, 15, 12, 20, 13:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 470 71215 0130 131520 0200', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('47 712 12 1315 1512 2015', cpls.get())

    def test_glr_add6(self):
        bt = BinaryTree()
        for i in 7, 4, 15, 12, 20, 10:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 4710 0100 71215 01520 0200', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('47 712 107 12 1512 2015', cpls.get())

    def test_glr_remove1(self):
        bt = BinaryTree()
        for i in 10, 5, 20, 2, 7, 15, 30, 1, 12, 25, 40, 22:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('12', bt.remove(12))
        self.assertEqual('010 120 257 070 51025 0150 152022 0220 202530 03040 0400', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3], [0, 0],
                          [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 25 510 75 10 1520 2025 2220 2510 3025 4030', cpls.get())

    def test_glr_remove2(self):
        bt = BinaryTree()
        for i in 10, 5, 20, 2, 7, 15, 30, 1, 19, 25, 40, 22:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('20', bt.remove(20))
        self.assertEqual('010 120 257 070 51025 0150 151922 0220 192530 03040 0400', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3], [0, 0],
                          [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 25 510 75 10 1519 1925 2219 2510 3025 4030', cpls.get())
