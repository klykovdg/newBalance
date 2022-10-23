import unittest
from app.binary_tree.BinaryTree import BinaryTree


class BinaryTreeGetTest(unittest.TestCase):
    def test_get1(self):
        bt = BinaryTree()
        k_arr = [3, 5, 7, 12, 1, 2, 6, 8]
        v_arr = ['three', 5, 'hi, Jack', 6.6, 'one', -2, None, 0]
        for i in range(len(k_arr)):
            bt.add(k_arr[i], v_arr[i])
        self.assertEqual(6.6, bt.get(12))
        self.assertEqual(5, bt.get(5))
        self.assertEqual('one', bt.get(1))
        self.assertEqual('hi, Jack', bt.get(7))
        self.assertEqual('three', bt.get(3))
        self.assertEqual(-2, bt.get(2))
        self.assertEqual(0, bt.get(8))
        self.assertEqual(None, bt.get(6))
        self.assertEqual('hi, Jack', bt.get(7))

    def test_there_is_no_such_key(self):
        bt = BinaryTree()
        self.assertIsNone(bt.get(5))

    def test_key_None(self):
        bt = BinaryTree()
        bt.add(10, '')
        self.assertIsNone(bt.get(None))
