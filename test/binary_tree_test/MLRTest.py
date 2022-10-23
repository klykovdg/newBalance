import unittest
from app.tools.TreeString import TreeString
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.GetterSubtreeLens import GetterSubtreeLens
from app.tools.ChildParentLinksString import ChildParentLinksString


class BinaryTreeTestMLR(unittest.TestCase):
    def test_mlr_add1(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 15:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 4712 090 91215 0150', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('47 7 912 127 1512', cpls.get())

    def test_mlr_remove1(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 1, 25, 40, 35, 45:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('25', bt.remove(25))
        self.assertEqual('010 1100 102040 03035 0350 304045 0450', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('110 1020 20 3040 3530 4020 4540', cpls.get())

    def test_mlr_remove2(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 1, 25, 40, 45:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('25', bt.remove(25))
        self.assertEqual('010 1100 102040 0300 304045 0450', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('110 1020 20 3040 4020 4540', cpls.get())

    def test_mlr_remove3(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 5, 28, 40, 45:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('30', bt.remove(30))
        self.assertEqual('050 5100 102040 0280 284045 0450', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 20 2840 4020 4540', cpls.get())

    def test_mlr_add2(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 2, 8, 10, 15, 17:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 240 4712 080 8910 0100 91215 01517 0170', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('24 47 7 89 912 109 127 1512 1715', cpls.get())

    def test_mlr_add3(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 2, 8, 10, 15, 14:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 240 4712 080 8910 0100 91215 0140 14150', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 0]], gsl.get())
        self.assertEqual('24 47 7 89 912 109 127 1415 1512', cpls.get())

    def test_mlr_remove4(self):
        bt = BinaryTree()
        for i in 30, 40, 20, 10, 25, 50, 35, 1, 33, 45, 60, 70, 43:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('33', bt.remove(33))
        self.assertEqual('010 1100 102025 0250 203050 0350 354045 0430 43450 405060 06070 0700', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 4], [0, 0], [1, 2],
                          [0, 0], [1, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('110 1020 2030 2520 30 3540 4050 4345 4540 5030 6050 7060', cpls.get())

    def test_mlr_remove5(self):
        bt = BinaryTree()
        for i in 30, 40, 20, 10, 25, 50, 35, 1, 33, 45, 60, 70, 59:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('33', bt.remove(33))
        self.assertEqual('010 1100 102025 0250 203050 0350 354045 0450 405060 0590 596070 0700', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3], [0, 0], [1, 1],
                          [0, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('110 1020 2030 2520 30 3540 4050 4540 5030 5960 6050 7060', cpls.get())

    def test_mlr_remove6(self):
        bt = BinaryTree()
        for i in 30, 40, 20, 10, 25, 50, 35, 1, 39, 45, 60, 47, 59:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('40', bt.remove(40))
        self.assertEqual('010 1100 102025 0250 203050 0350 353945 04547 0470 395060 0590 59600', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 4], [0, 0],
                          [1, 2], [0, 1], [0, 0], [3, 2], [0, 0], [1, 0]], gsl.get())
        self.assertEqual('110 1020 2030 2520 30 3539 3950 4539 4745 5030 5960 6050', cpls.get())

    def test_mlr_add4(self):
        bt = BinaryTree()
        for i in 7, 9, 12:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('070 7912 0120', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('79 9 129', cpls.get())

    def test_mlr_remove7(self):
        bt = BinaryTree()
        for i in 5, 3, 7, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('3', bt.remove(3))
        self.assertEqual('050 5710 0100', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('57 7 107', cpls.get())

    def test_mlr_remove8(self):
        bt = BinaryTree()
        for i in 5, 3, 7, 6, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('3', bt.remove(3))
        self.assertEqual('056 060 5710 0100', ts.get())
        self.assertEqual([[0, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('57 65 7 107', cpls.get())

    def test_mlr_remove9(self):
        bt = BinaryTree()
        for i in 5, 4, 8, 7, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('5', bt.remove(5))
        self.assertEqual('047 070 4810 0100', ts.get())
        self.assertEqual([[0, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('48 74 8 108', cpls.get())

    def test_mlr_add5(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 8, 10, 12:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 478 080 7910 01012 0120', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('47 79 87 9 109 1210', cpls.get())

    def test_mlr_add6(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 12, 8, 10:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('040 478 080 7912 0100 10120', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 0]], gsl.get())
        self.assertEqual('47 79 87 9 1012 129', cpls.get())

    def test_mlr_remove10(self):
        bt = BinaryTree()
        for i in 10, 5, 20, 1, 15, 25, 13, 30:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('1', bt.remove(1))
        self.assertEqual('050 51015 0130 13150 102025 02530 0300', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 1315 1510 20 2520 3025', cpls.get())

    def test_mlr_remove11(self):
        bt = BinaryTree()
        for i in 10, 5, 20, 1, 15, 25, 30:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('1', bt.remove(1))
        self.assertEqual('050 51015 0150 102025 02530 0300', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 1510 20 2520 3025', cpls.get())

    def test_mlr_remove12(self):
        bt = BinaryTree()
        for i in 10, 6, 20, 1, 15, 25, 30:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('10', bt.remove(10))
        self.assertEqual('010 1615 0150 62025 02530 0300', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('16 620 156 20 2520 3025', cpls.get())

    def test_mlr_remove13(self):
        bt = BinaryTree()
        for i in 20, 10, 40, 5, 16, 30, 50, 15, 25, 33, 45, 60, 62:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('20', bt.remove(20))
        self.assertEqual('050 51015 0150 101630 0250 253033 0330 164050 0450 455060 06062 0620', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 1],
                          [0, 0], [3, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1016 1510 1640 2530 3016 3330 40 4550 5040 6050 6260', cpls.get())

    def test_mlr_remove_double(self):
        bt = BinaryTree()
        for i in 30, 20, 50, 19, 25, 40, 60, 26, 45, 55, 70, 54:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('20', bt.remove(20))
        self.assertEqual('0190 192526 0260 253040 04045 0450 305060 0540 54550 556070 0700', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1],
                          [0, 0], [3, 3], [0, 0], [1, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('1925 2530 2625 3050 4030 4540 50 5455 5560 6050 7060', cpls.get())
