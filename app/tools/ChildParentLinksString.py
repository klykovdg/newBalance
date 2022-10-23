from app.binary_tree.BinaryTree import BinaryTree


class ChildParentLinksString:
    """
    The single method of the class returns string of vertexes and their parents
    from the least one to the greatest one.
    A vertex and its parent are space apart from another vertex and its parent.
    If there is no parent (root) a vertex is writen alone.
    If a tree is empty the method "get" returns ''
    """
    def __init__(self, tree: BinaryTree):
        self._tree = tree
        self._arr = []

    def get(self):
        if self._tree.root:
            self._arr = []
            self._get_string_of_child_parent_links(self._tree.root)
            self._arr[-1] = self._arr[-1].strip()
            return ''.join(self._arr)
        return ''

    def _get_string_of_child_parent_links(self, node):
        if node.left:
            self._get_string_of_child_parent_links(node.left)
        child = str(node.k)
        parent = str(node.parent.k) if node.parent else ''
        self._arr.append(child + parent + ' ')
        if node.right:
            self._get_string_of_child_parent_links(node.right)
