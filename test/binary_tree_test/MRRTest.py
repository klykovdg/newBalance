import unittest
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.TreeString import TreeString
from app.tools.GetterSubtreeLens import GetterSubtreeLens
from app.tools.ChildParentLinksString import ChildParentLinksString


class BinaryTreeMRRTest(unittest.TestCase):
    def test_mrr_add1(self):
        bt = BinaryTree()
        for i in 7, 4, 9, 3, 2:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 234 040 379 090', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('23 37 43 7 97', cpls.get())

    def test_mrr_add2(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 12, 4, 9, 2, 1:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 124 040 289 090 81011 01112 0120', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 1], [0, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 28 42 810 98 10 1110 1211', cpls.get())

    def test_mrr_remove1(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 6, 15, 36, 4, 8:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('15', bt.remove(15))
        self.assertEqual('040 4610 080 8100 62030 03036 0360', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('46 620 810 106 20 3020 3630', cpls.get())

    def test_mrr_remove2(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 6, 15, 36, 4:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('15', bt.remove(15))
        self.assertEqual('040 4610 0100 62030 03036 0360', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('46 620 106 20 3020 3630', cpls.get())

    def test_mrr_remove3(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 60, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('30', bt.remove(30))
        self.assertEqual('0100 102035 0350 204050 05060 0600', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 2040 3520 40 5040 6050', cpls.get())

    def test_mrr_add3(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 12, 4, 9, 2, 5, 1:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('010 120 248 050 589 090 41011 01112 0120', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('12 24 410 58 84 98 10 1110 1211', cpls.get())

    def test_mrr_add4(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 12, 4, 9, 2, 5, 3:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('023 030 248 050 589 090 41011 01112 0120', ts.get())
        self.assertEqual([[0, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0, 0], [3, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('24 32 410 58 84 98 10 1110 1211', cpls.get())

    def test_mrr_remove4(self):
        bt = BinaryTree()
        for i in 30, 20, 40, 10, 25, 35, 50, 5, 15, 27, 60, 1, 17:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('27', bt.remove(27))
        self.assertEqual('010 150 51020 01517 0170 152025 0250 103040 0350 354050 05060 0600', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 1], [0, 0], [2, 1],
                          [0, 0], [4, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('15 510 1030 1520 1715 2010 2520 30 3540 4030 5040 6050', cpls.get())

    def test_mrr_remove5(self):
        bt = BinaryTree()
        for i in 30, 20, 40, 10, 25, 35, 50, 5, 15, 27, 60, 1, 7:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('27', bt.remove(27))
        self.assertEqual('010 157 070 51020 0150 152025 0250 103040 0350 354050 05060 0600', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0, 0],
                          [3, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('15 510 75 1030 1520 2010 2520 30 3540 4030 5040 6050', cpls.get())

    def test_mrr_remove6(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 45, 60, 10, 25, 32, 70, 12, 23:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('30', bt.remove(30))
        self.assertEqual('01012 0120 102032 0230 23250 253235 0350 204050 0450 455060 06070 0700', ts.get())
        self.assertEqual([[0, 1], [0, 0], [2, 3], [0, 0], [1, 0], [2, 1], [0, 0],
                          [4, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 1210 2040 2325 2532 3220 3532 40 4550 5040 6050 7060', cpls.get())

    def test_mrr_add5(self):
        bt = BinaryTree()
        for i in 7, 5, 3:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('030 357 070', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('35 5 75', cpls.get())

    def test_mrr_remove7(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 4:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('11', bt.remove(11))
        self.assertEqual('040 4810 0100', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('48 8 108', cpls.get())

    def test_mrr_remove8(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 4, 9:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('11', bt.remove(11))
        self.assertEqual('040 4810 090 9100', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 0]], gsl.get())
        self.assertEqual('48 8 910 108', cpls.get())

    def test_mrr_remove9(self):
        bt = BinaryTree()
        for i in 10, 5, 11, 3, 7:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('10', bt.remove(10))
        self.assertEqual('030 3511 070 7110', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 0]], gsl.get())
        self.assertEqual('35 5 711 115', cpls.get())

    def test_mrr_add6(self):
        bt = BinaryTree()
        for i in 9, 5, 10, 4, 7, 2:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('020 240 459 070 7910 0100', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('24 45 5 79 95 109', cpls.get())

    def test_mrr_add7(self):
        bt = BinaryTree()
        for i in 9, 6, 10, 4, 7, 5:
            bt.add(i, '')
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('045 050 469 070 7910 0100', ts.get())
        self.assertEqual([[0, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('46 54 6 79 96 109', cpls.get())

    def test_mrr_remove10(self):
        bt = BinaryTree()
        for i in 30, 20, 40, 10, 24, 50, 5, 26:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('50', bt.remove(50))
        self.assertEqual('050 5100 102030 02426 0260 243040 0400', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 1], [0, 0], [2, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 20 2430 2624 3020 4030', cpls.get())

    def test_mrr_remove11(self):
        bt = BinaryTree()
        for i in 30, 20, 40, 10, 24, 50, 5:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('50', bt.remove(50))
        self.assertEqual('050 5100 102030 0240 243040 0400', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 20 2430 3020 4030', cpls.get())

    def test_mrr_remove12(self):
        bt = BinaryTree()
        for i in 40, 30, 45, 20, 35, 60, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('40', bt.remove(40))
        self.assertEqual('0100 102030 0300 203545 04560 0600', ts.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 2035 3020 35 4535 6045', cpls.get())

    def test_mrr_remove13(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 41, 60, 10, 25, 32, 37, 45, 5:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('40', bt.remove(40))
        self.assertEqual('050 5100 102025 0250 203041 0320 323537 0370 354150 0450 455060 0600', ts.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3], [0, 0],
                          [1, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('510 1020 2030 2520 30 3235 3541 3735 4130 4550 5041 6050', cpls.get())

    def test_mrr_remove_double(self):
        bt = BinaryTree()
        for i in 40, 30, 50, 20, 35, 45, 51, 10, 25, 32, 42, 27:
            bt.add(i, str(i))
        ts = TreeString(bt)
        gsl = GetterSubtreeLens(bt)
        cpls = ChildParentLinksString(bt)
        self.assertEqual('50', bt.remove(50))
        self.assertEqual('0100 102025 02527 0270 203040 0320 32350 354045 0420 424551 0510', ts.get())
        self.assertEqual([[0, 0], [1, 2], [0, 1], [0, 0], [3, 3], [0, 0],
                          [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())
        self.assertEqual('1020 2030 2520 2725 30 3235 3540 4030 4245 4540 5145', cpls.get())
