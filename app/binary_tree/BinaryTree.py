from app.binary_tree.Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None
        self._val_searched = None
        self._val_removed = None
        self._removed_vertex_pos = 0
        self._nearest_left_v_pos = 1
        self._nearest_right_v_pos = 2
        self._key_is_not_found = True

    def add(self, key, value):
        if key:
            if self.root:
                self._compare_and_add(self.root, key, value)
            else:
                self.root = Node(key, value)

    def get(self, key):
        if key:
            self._val_searched = None
            self._get_val(key, self.root)
            return self._val_searched
        return None

    def remove(self, key):
        if key:
            self._val_removed = None
            self._remove_node(key, self.root)
            self._key_is_not_found = True
            return self._val_removed
        return None

    def _compare_and_add(self, parent, k, v):
        if k > parent.k:
            if parent.right:
                self._compare_and_add(parent.right, k, v)
            else:  # parent.right == None
                node = Node(k, v)
                parent.right = node
                node.parent = parent
            if parent.len_right_subtree == max(parent.right.len_left_subtree, parent.right.len_right_subtree):
                parent.len_right_subtree += 1
        elif k < parent.k:
            if parent.left:
                self._compare_and_add(parent.left, k, v)
            else:
                node = Node(k, v)
                parent.left = node
                node.parent = parent
            if parent.len_left_subtree == max(parent.left.len_left_subtree, parent.left.len_right_subtree):
                parent.len_left_subtree += 1
        else:
            return
        if abs(parent.len_left_subtree - parent.len_right_subtree) == 2:
            self._do_balance(parent)

    def _do_balance(self, node):
        if node.len_right_subtree > node.len_left_subtree:
            n = node.right
            if n.len_right_subtree >= n.len_left_subtree:
                self._mlr(node)
            else:
                self._glr(node)
        else:
            n = node.left
            if n.len_left_subtree >= n.len_right_subtree:
                self._mrr(node)
            else:
                self._grr(node)

    def _mlr(self, node):  # minor left rotation
        gparent = node.parent
        right_subtree = node.right
        node.right = right_subtree.left  # left subtree of right subtree becomes right subtree of node
        if node.right:
            node.len_right_subtree = max(node.right.len_left_subtree, node.right.len_right_subtree) + 1
            node.right.parent = node
        else:
            node.len_right_subtree = 0

        if gparent:
            right_subtree.parent = gparent  # right subtree becomes left child of grandparent or root
            if node == gparent.left:
                gparent.left = right_subtree
            else:  # right subtree becomes right child of grandparent
                gparent.right = right_subtree
        else:
            right_subtree.parent = None
            self.root = right_subtree
        right_subtree.left = node  # node becomes left subtree of right subtree
        node.parent = right_subtree
        if right_subtree.left:
            right_subtree.len_left_subtree = max(right_subtree.left.len_right_subtree,
                                                 right_subtree.left.len_left_subtree) + 1
        if right_subtree.right:
            right_subtree.len_right_subtree = max(right_subtree.right.len_right_subtree,
                                                  right_subtree.right.len_left_subtree) + 1

    def _mrr(self, node):
        gparent = node.parent
        left_subtree = node.left
        node.left = left_subtree.right  # right subtree of left subtree becomes left subtree of node
        if node.left:
            node.len_left_subtree = max(node.left.len_left_subtree, node.left.len_right_subtree) + 1
            node.left.parent = node
        else:
            node.len_left_subtree = 0

        if gparent:
            left_subtree.parent = gparent  # left subtree becomes left child of grandparent or root
            if node == gparent.left:
                gparent.left = left_subtree
            else:  # left subtree becomes right child of grandparent
                gparent.right = left_subtree
        else:
            left_subtree.parent = None
            self.root = left_subtree
        left_subtree.right = node  # node becomes right subtree of left subtree
        node.parent = left_subtree
        if left_subtree.left:
            left_subtree.len_left_subtree = max(left_subtree.left.len_right_subtree,
                                                left_subtree.left.len_left_subtree) + 1
        if left_subtree.right:
            left_subtree.len_right_subtree = max(left_subtree.right.len_right_subtree,
                                                 left_subtree.right.len_left_subtree) + 1

    def _glr(self, node):  # grand left rotation
        self._mrr(node.right)
        self._mlr(node)

    def _grr(self, node):
        self._mlr(node.left)
        self._mrr(node)

    def _get_val(self, key, node):
        if node:
            if key > node.k:
                self._get_val(key, node.right)
            elif key < node.k:
                self._get_val(key, node.left)
            else:
                self._val_searched = node.v
        else:
            self._val_searched = None

    def _remove_node(self, k, node):
        if node:
            if k > node.k:
                self._remove_node(k, node.right)
                if node.right:
                    node.len_right_subtree = max(node.right.len_right_subtree, node.right.len_left_subtree) + 1
                else:
                    node.len_right_subtree = 0
            elif k < node.k:
                self._remove_node(k, node.left)
                if node.left:
                    node.len_left_subtree = max(node.left.len_right_subtree, node.left.len_left_subtree) + 1
                else:
                    node.len_left_subtree = 0
            else:
                if self._key_is_not_found:
                    self._val_removed = node.v
                    self._key_is_not_found = False
                self._is_leaf_or_vert(node)
                return
            if abs(node.len_left_subtree - node.len_right_subtree) == 2:
                self._do_balance(node)
        else:
            self._val_removed = None

    def _is_leaf_or_vert(self, node):
        if not node.left and not node.right:
            self._remove_leaf(node)
        else:
            nodes = [0] * 3  # will contain removed node (0), the nearest left (1) and right (2) nodes
            nodes[self._removed_vertex_pos] = node
            self._remove_vertex(nodes)

    def _remove_leaf(self, node):
        if node.parent:
            if node.parent.right:
                if node.parent.right == node:
                    node.parent.right = None
                    return
            node.parent.left = None
        else:
            self.root = None

    def _remove_vertex(self, nodes):
        pos = self._removed_vertex_pos
        if nodes[pos].left:
            self._find_the_last_right_node_of_the_left_subtree(nodes, nodes[pos].left)
        if nodes[pos].right:
            self._find_the_last_left_node_of_the_right_subtree(nodes, nodes[pos].right)
        self._choose_substitution(nodes)

    def _find_the_last_right_node_of_the_left_subtree(self, nodes, current_node):
        if current_node.right:
            self._find_the_last_right_node_of_the_left_subtree(nodes, current_node.right)
        else:
            nodes[self._nearest_left_v_pos] = current_node

    def _find_the_last_left_node_of_the_right_subtree(self, nodes, current_node):
        if current_node.left:
            self._find_the_last_left_node_of_the_right_subtree(nodes, current_node.left)
        else:
            nodes[self._nearest_right_v_pos] = current_node

    def _choose_substitution(self, nodes):
        """
        When (rnode.k - l.k) == (r.k - rnode.k) and both are the leafs,
        the algorithm chooses the left node as the substitution.
        According to the statistic, it may be worth to do it vice versa
        but this is another question the further studying
        """
        rnode = nodes[self._removed_vertex_pos]
        l = nodes[self._nearest_left_v_pos]
        r = nodes[self._nearest_right_v_pos]
        if l and r:
            if (rnode.k - l.k) < (r.k - rnode.k):
                subst = l
            elif (rnode.k - l.k) > (r.k - rnode.k):
                subst = r
            else:
                subst = l if not l.right and not l.left else r
        else:
            subst = l if l else r
        self._remove_node(subst.k, rnode)
        self._substitute(rnode, subst)

    def _substitute(self, removed_v, substitution):
        if removed_v.parent:
            substitution.parent = removed_v.parent
            if substitution.parent.right == removed_v:
                substitution.parent.right = substitution
            else:
                substitution.parent.left = substitution
            removed_v.parent = None
        else:
            self.root = substitution
            substitution.parent = None
        if removed_v.right:
            substitution.right = removed_v.right
            substitution.right.parent = substitution
            removed_v.right = None
        if removed_v.left:
            substitution.left = removed_v.left
            substitution.left.parent = substitution
            removed_v.left = None
        substitution.len_left_subtree = removed_v.len_left_subtree
        substitution.len_right_subtree = removed_v.len_right_subtree
