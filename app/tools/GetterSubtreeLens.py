from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node


class GetterSubtreeLens:
    """
    The single method of this class returns a list of lists.
    Each list contains 2 elements. It is the depth of the left and the right subtrees of a vertex.
    The first list contains subtrees of the least vertex.
    The last one contains subtrees of the greatest vertex.
    If a vertex has no subtrees its list contains two 0
    If a tree is empty the method "get" returns []
    """
    def __init__(self, tree: BinaryTree):
        self._tree = tree
        self._arr = []

    def get(self):
        self._arr = []
        if self._tree.root:
            self._get_arr_subtree_lens(self._tree.root)
        return self._arr

    def _get_arr_subtree_lens(self, node: Node):
        if node.left:
            self._get_arr_subtree_lens(node.left)
        self._arr.append([node.len_left_subtree, node.len_right_subtree])
        if node.right:
            self._get_arr_subtree_lens(node.right)
