class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.parent = None
        self.left = None
        self.right = None
        self.len_left_subtree = 0
        self.len_right_subtree = 0
