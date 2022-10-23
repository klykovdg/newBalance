import unittest
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.TreeString import TreeString
from app.tools.ChildParentLinksString import ChildParentLinksString
from app.tools.GetterSubtreeLens import GetterSubtreeLens


class RemoveTest(unittest.TestCase):
    def test_remove1(self):
        bt = BinaryTree()
        for i in 7, 3, 9:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('9', bt.remove(9))
        self.assertEqual('030 370', ts.get())
        self.assertEqual('37 7', cpls.get())
        self.assertEqual([[0, 0], [1, 0]], gsl.get())

        self.assertEqual('3', bt.remove(3))
        self.assertEqual('070', ts.get())
        self.assertEqual('7', cpls.get())
        self.assertEqual([[0, 0]], gsl.get())

    def test_remove2(self):
        bt = BinaryTree()
        for i in 10, 8, 11, 2, 9, 12:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('11', bt.remove(11))
        self.assertEqual('020 289 090 81012 0120', ts.get())
        self.assertEqual('28 810 98 10 1210', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0], [2, 1], [0, 0]], gsl.get())

        self.assertEqual('8', bt.remove(8))
        self.assertEqual('020 290 91012 0120', ts.get())
        self.assertEqual('29 910 10 1210', cpls.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0]], gsl.get())

        self.assertEqual(bt.remove(2), '2')
        self.assertEqual('090 91012 0120', ts.get())
        self.assertEqual('910 10 1210', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_remove3(self):
        bt = BinaryTree()
        for i in 100, 25, 500, 15, 40, 350, 506, 20, 33, 70, 155, 400, 705, 27, 37:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('25', bt.remove(25))
        self.assertEqual('01520 0200 152740 03337 0370 334070 0700 27100500 '
                         '01550 155350400 04000 350500506 0506705 07050', ts.get())
        self.assertEqual('1527 2015 27100 3340 3733 4027 7040 100 155350 '
                         '350500 400350 500100 506500 705506', cpls.get())
        self.assertEqual([[0, 1], [0, 0], [2, 3], [0, 1], [0, 0], [2, 1], [0, 0],
                          [4, 3], [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('37', bt.remove(37))
        self.assertEqual('01520 0200 152740 0330 334070 0700 27100500 '
                         '01550 155350400 04000 350500506 0506705 07050', ts.get())
        self.assertEqual('1527 2015 27100 3340 4027 7040 100 155350 '
                         '350500 400350 500100 506500 705506', cpls.get())
        self.assertEqual([[0, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0, 0],
                          [3, 3], [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('100', bt.remove(100))
        self.assertEqual('01520 0200 152740 0330 33400 2770500 '
                         '01550 155350400 04000 350500506 0506705 07050', ts.get())
        self.assertEqual('1527 2015 2770 3340 4027 70 155350 '
                         '350500 400350 50070 506500 705506', cpls.get())
        self.assertEqual([[0, 1], [0, 0], [2, 2], [0, 0], [1, 0], [3, 3],
                          [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('500', bt.remove(500))
        self.assertEqual('01520 0200 152740 0330 33400 2770506 '
                         '01550 155350400 04000 350506705 07050', ts.get())
        self.assertEqual('1527 2015 2770 3340 4027 70 155350 '
                         '350506 400350 50670 705506', cpls.get())
        self.assertEqual([[0, 1], [0, 0], [2, 2], [0, 0], [1, 0], [3, 3],
                          [0, 0], [1, 1], [0, 0], [2, 1], [0, 0]], gsl.get())

    def test_remove4(self):
        bt = BinaryTree()
        for i in 10, 5, 15, 1, 20:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('20', bt.remove(20))
        self.assertEqual('010 150 51015 0150', ts.get())
        self.assertEqual('15 510 10 1510', cpls.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0]], gsl.get())

        self.assertEqual('1', bt.remove(1))
        self.assertEqual('050 51015 0150', ts.get())
        self.assertEqual('510 10 1510', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_remove5(self):
        bt = BinaryTree()
        for i in 10, 5, 15, 1, 20:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('5', bt.remove(5))
        self.assertEqual('010 11015 01520 0200', ts.get())
        self.assertEqual('110 10 1510 2015', cpls.get())
        self.assertEqual([[0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('15', bt.remove(15))
        self.assertEqual('010 11020 0200', ts.get())
        self.assertEqual('110 10 2010', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_remove6(self):
        bt = BinaryTree()
        for i in 50, 25, 75, 24, 35, 60, 76, 1, 30, 40, 55, 62, 80:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('25', bt.remove(25))
        self.assertEqual('010 12435 0300 303540 0400 245075 0550 556062 0620 607576 07680 0800', ts.get())
        self.assertEqual('124 2450 3035 3524 4035 50 5560 6075 6260 7550 7675 8076', cpls.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 1], [0, 0], [3, 3],
                          [0, 0], [1, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('75', bt.remove(75))
        self.assertEqual('010 12435 0300 303540 0400 245076 0550 556062 0620 607680 0800', ts.get())
        self.assertEqual('124 2450 3035 3524 4035 50 5560 6076 6260 7650 8076', cpls.get())
        self.assertEqual([[0, 0], [1, 2], [0, 0], [1, 1], [0, 0], [3, 3],
                          [0, 0], [1, 1], [0, 0], [2, 1], [0, 0]], gsl.get())

    def test_remove7(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 5, 17, 29, 35, 1, 15, 28, 31, 40:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('10', bt.remove(10))
        self.assertEqual('010 150 51517 0170 152030 0280 28290 293035 0310 313540 0400', ts.get())
        self.assertEqual('15 515 1520 1715 20 2829 2930 3020 3135 3530 4035', cpls.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3],
                          [0, 0], [1, 0], [2, 2], [0, 0], [1, 1], [0, 0]], gsl.get())

        self.assertEqual('30', bt.remove(30))
        self.assertEqual('010 150 51517 0170 152031 0280 28290 293135 03540 0400', ts.get())
        self.assertEqual('15 515 1520 1715 20 2829 2931 3120 3531 4035', cpls.get())
        self.assertEqual([[0, 0], [1, 0], [2, 1], [0, 0], [3, 3],
                          [0, 0], [1, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

    def test_remove8(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 5, 13, 25, 34, 7, 15, 26, 39:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('10', bt.remove(10))
        self.assertEqual('050 5713 01315 0150 72030 02526 0260 253034 03439 0390', ts.get())
        self.assertEqual('57 720 137 1513 20 2530 2625 3020 3430 3934', cpls.get())
        self.assertEqual([[0, 0], [1, 2], [0, 1], [0, 0], [3, 3], [0, 1], [0, 0], [2, 2], [0, 1], [0, 0]], gsl.get())

        self.assertEqual('30', bt.remove(30))
        self.assertEqual('050 5713 01315 0150 72026 0250 252634 03439 0390', ts.get())
        self.assertEqual('57 720 137 1513 20 2526 2620 3426 3934', cpls.get())
        self.assertEqual([[0, 0], [1, 2], [0, 1], [0, 0], [3, 3], [0, 0], [1, 2], [0, 1], [0, 0]], gsl.get())

    def test_remove_none1(self):
        bt = BinaryTree()
        for i in 7, 3, 9:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertIsNone(bt.remove(None))
        self.assertEqual('030 379 090', ts.get())
        self.assertEqual('37 7 97', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_remove_none2(self):
        bt = BinaryTree()
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertIsNone(bt.remove(11))
        self.assertEqual('', ts.get())
        self.assertEqual('', cpls.get())
        self.assertEqual([], gsl.get())

    def test_remove_none3(self):
        bt = BinaryTree()
        for i in 7, 3, 9:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertIsNone(bt.remove(11))
        self.assertEqual('030 379 090', ts.get())
        self.assertEqual('37 7 97', cpls.get())
        self.assertEqual([[0, 0], [1, 1], [0, 0]], gsl.get())

    def test_remove_root1(self):
        bt = BinaryTree()
        for i in 7, 3, 9:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('7', bt.remove(7))
        self.assertEqual('030 390', ts.get())
        self.assertEqual('39 9', cpls.get())
        self.assertEqual([[0, 0], [1, 0]], gsl.get())

    def test_remove_root2(self):
        bt = BinaryTree()
        for i in 7, 6, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('7', bt.remove(7))
        self.assertEqual('0610 0100', ts.get())
        self.assertEqual('6 106', cpls.get())
        self.assertEqual([[0, 1], [0, 0]], gsl.get())

    def test_remove_root4(self):
        bt = BinaryTree()
        bt.add(7, '7')
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('7', bt.remove(7))
        self.assertEqual('', ts.get())
        self.assertEqual('', cpls.get())
        self.assertEqual([], gsl.get())
        bt.add(9, '9')
        self.assertEqual('090', ts.get())
        self.assertEqual('9', cpls.get())
        self.assertEqual([[0, 0]], gsl.get())

    def test_remove_both_leaves1(self):
        bt = BinaryTree()
        for i in 7, 4, 10:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('7', bt.remove(7))
        self.assertEqual('0410 0100', ts.get())
        self.assertEqual('4 104', cpls.get())
        self.assertEqual([[0, 1], [0, 0]], gsl.get())

    def test_remove_both_leaves2(self):
        bt = BinaryTree()
        for i in 20, 10, 30, 5, 25, 35, 26, 34:
            bt.add(i, str(i))
        ts = TreeString(bt)
        cpls = ChildParentLinksString(bt)
        gsl = GetterSubtreeLens(bt)
        self.assertEqual('30', bt.remove(30))
        self.assertEqual('050 5100 102026 0250 252635 0340 34350', ts.get())
        self.assertEqual('510 1020 20 2526 2620 3435 3526', cpls.get())
        self.assertEqual([[0, 0], [1, 0], [2, 3], [0, 0], [1, 2], [0, 0], [1, 0]], gsl.get())
