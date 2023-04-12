from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node


class TreeString:
    """
    A class prints a tree as one line from the vertex with the least key
    to the vertex with the greatest key. A key represents a vertex.
    If a vertex has no children they're written as 0
    Each vertex and its children
    (the left child to the left; the vertex in the middle; the right one to the right)
    are space apart from another vertex and its children.
    If a tree is empty the method "get" returns ''
    """
    def __init__(self, tree: BinaryTree):
        self._tree = tree
        self._arr = []

    def some(self):
        pass

    def get(self):
        if self._tree.root:
            self._arr = []
            self._flatten_tree(self._tree.root)
            self._arr[-1] = self._arr[-1].strip()
            return ''.join(self._arr)
        return ''

    def _flatten_tree(self, node: Node):
        if node.left:
            self._flatten_tree(node.left)
        n = str(node.k)
        l = str(node.left.k) if node.left else '0'
        r = str(node.right.k) if node.right else '0'
        self._arr.append(l + n + r + ' ')  # it can be a billion vertices but only 2 children of one vertex
        if node.right:
            self._flatten_tree(node.right)
