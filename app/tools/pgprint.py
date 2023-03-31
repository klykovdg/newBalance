from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node


_result = []
_root = None
_t = str('\u2524')        # ┤
_r = str('\u250C')        # ┌
_r_versa = str('\u2510')  # ┐
_l = str('\u2514')        # └
_l_versa = str('\u2518')  # ┘
_pole = str('\u2502')     # │


def pgprint(bt: BinaryTree):
    global _root, _result
    _result = []
    _root = bt.root
    if _root:
        _find_lowest_and_print(_root)
    print(''.join(_result))


def _find_lowest_and_print(node: Node):
    """
    Starts to print (add line by line into result list) graph from up to down,
    from the lowest node in the graph to the biggest
    """
    if node.left:
        _find_lowest_and_print(node.left)
    _compose_line_and_add_into_result_list(node)
    if node.right:
        _find_lowest_and_print(node.right)


def _compose_line_and_add_into_result_list(node: Node):
    current_line = _get_poles_and_spaces(node) + _get_rest(node) + '\n'
    _result.append(current_line)


def _get_poles_and_spaces(node: Node):
    """
    As pgprint starts to print graph from up to down this method should compute
    how many space and poles are before node.
    A turn means that you have some init value, and the second value.
    If the third value will be more than the first but less than the second
    (or the third value will be less than the first but more than the second)
    it means that the turn has happened and a pole must appear.
          ┌1
        ┌2┤
        │ └3
      ┌4┤
      │ └5┐
      │   └7
    10┤
    Let's consider the second line "    ┌2┤"
    init = 10, second = 4, third = 2
    There is no any turn. That's why there is no need to add any poles before "┌2┤"
    Let's consider the third line "     │ └3"
    init = 4, second = 2, third = 3
    A turn has happened from 2 to 3. The current line "     " should add a pole and
    spaces equal the length of key (2 spaces for number 89, one for 7, three for 789 and so on) "│ └3"
    """

    if node == _root:
        return ''

    poles_and_spaces = ''  # value which will be returned
    path: list = _get_path_from_root_to_node(node)  # list of nodes
    flags = [False, False]  # it needs for turning

    for i in range(1, len(path)):
        prev = path[i - 1]
        if prev.k > path[i].k:
            flags[1] = True
            cur_flag_index = 0
        else:
            flags[0] = True
            cur_flag_index = 1

        if flags[cur_flag_index]:  # "True" means that a turn has happened
            poles_and_spaces += _pole
            poles_and_spaces += _get_spaces(prev)
            flags[cur_flag_index] = False
        else:  # There was no any turn
            spaces = _get_spaces(prev)
            if prev == _root:
                poles_and_spaces += spaces
            else:
                poles_and_spaces += spaces + " "  # needs addit-al space due to trailing symbol (in line #6 due to "4┤")
    return poles_and_spaces


def _get_path_from_root_to_node(node: Node):
    """
    :return: the list of nodes from root to searched node
    """
    path = []
    _find_path_from_root_to_node(node, _root, path)
    return path


def _find_path_from_root_to_node(end, current, path):
    path.append(current)
    if end.k == current.k:
        return

    if end.k < current.k:
        _find_path_from_root_to_node(end, current.left, path)
    elif end.k > current.k:
        _find_path_from_root_to_node(end, current.right, path)


def _get_spaces(node: Node):
    key = str(node.k)
    return ' ' * len(key)


def _get_rest(node: Node):
    symbol_before = _is_it_right_left_node_from_parent(node)
    symbol_after = _does_it_have_left_right_or_both_children(node)
    return symbol_before + str(node.k) + symbol_after


def _is_it_right_left_node_from_parent(node: Node):
    if node.parent:
        return _l if node == node.parent.right else _r
    return ''


def _does_it_have_left_right_or_both_children(node):
    if node.right:
        return _t if node.left else _r_versa
    return _l_versa if node.left else ''
