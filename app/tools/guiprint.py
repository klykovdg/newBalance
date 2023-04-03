from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node
from tkinter import *

# TODO check bt is None or empty
# TODO compute VARS according to the key size
_X1_START = 25
_X_NODE_SIZE = 50  # x2 - x1
_X_OFFSET = 25     # space between two nodes in X
_Y1_START = 50
_Y_NODE_SIZE = 50  # y2 - y1
_LINE = 50         # # space between two nodes in Y


def guiprint(bt: BinaryTree, parent=None):
    flag = False
    _config_globals(bt)
    if not parent:
        win = Tk()
        flag = True
    else:
        win = Toplevel(parent)
    _make_widgets(win)
    lines_coordinates = []
    _print_nodes(bt.root, _canvas, lines_coordinates)
    _print_lines(_canvas, lines_coordinates)
    _config_canvas(_canvas, bt)
    if flag:
        win.mainloop()


def _config_globals(bt: BinaryTree):
    global _depth_right_plunge, _keys
    _depth_right_plunge = 0
    _keys = _get_tree_keys(bt.root)


def _make_widgets(win):
    canvas = Canvas(win, bg='white', width=1000, height=500)
    yscroll = Scrollbar(win, command=canvas.yview)
    xscroll = Scrollbar(win, command=canvas.xview, orient='horizontal')
    canvas.config(yscrollcommand=yscroll.set)
    canvas.config(xscrollcommand=xscroll.set)
    xscroll.pack(side=BOTTOM, fill=X)
    canvas.pack(side=LEFT, expand=YES, fill=BOTH)
    yscroll.pack(side=RIGHT, fill=Y)
    global _canvas
    _canvas = canvas


def _config_canvas(canvas: Canvas, bt: BinaryTree):
    canvas.config(scrollregion=(0, 0, _get_x_max(), _get_y_max(bt.root)))
    canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))
    canvas.itemconfigure('line', width=3, fill='black')
    canvas.lower('line')
    canvas.itemconfigure('node', fill='#6bceff', outline='black', width=3)
    canvas.itemconfigure('text', fill='black', font=('roman', 13, 'normal'))


def _print_nodes(node: Node , canvas: Canvas, lines_coord, depth=0):
    if node.left:
        _print_nodes(node.left, canvas, lines_coord, depth + 1)
    column = _keys.index(node.k)
    y1, y2 = _get_y1_y2(depth)
    x1, x2 = _get_x1_x2(column)
    canvas.create_oval(x1, y1, x2, y2, tags='node')
    canvas.create_text(x1 + ((x2 - x1) / 2),
                       y1 + ((y2 - y1) / 2),
                       text=str(node.k), tags='text')

    global _depth_right_plunge
    if node.left:
        lines_coord.append(_get_own_coord(x1, y1, x2, y2))
    if node.right:
        if node.parent:
            lines_coord.append(_get_own_coord(x1, y1, x2, y2))
            lines_coord.append(_get_child_coordinates(column + 1, depth + 1))
            _depth_right_plunge += 1

    if node.right:
        _print_nodes(node.right, canvas, lines_coord, depth + 1)

    if _depth_right_plunge != 0:  # have all needed coordinates
        _depth_right_plunge -= 1
    else:
        lines_coord.append(_get_own_coord(x1, y1, x2, y2))


def _get_y1_y2(depth):
    y1 = _Y1_START + (_LINE + _Y_NODE_SIZE) * depth
    y2 = y1 + _Y_NODE_SIZE

    return y1, y2


def _get_x1_x2(column):
    x1 = _X1_START + (_X_OFFSET + _X_NODE_SIZE) * column
    x2 = x1 + _X_NODE_SIZE

    return x1, x2


def _get_own_coord(x1, y1, x2, y2):
    x = x1 + ((x2 - x1) / 2)
    y = y1 + ((y2 - y1) / 2)

    return x, y


def _get_child_coordinates(column, depth):
    x1, x2 = _get_x1_x2(column)
    x = x1 + ((x2 - x1) / 2)
    y1, y2 = _get_y1_y2(depth)
    y = y1 + ((y2 - y1) / 2)

    return x, y


def _print_lines(canvas: Canvas, coordinates: list):
    for i in range(0, len(coordinates), 2):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        canvas.create_line(x1, y1, x2, y2, tags='line')


def _get_y_max(root: Node):
    number_lines_with_nodes = (max(root.len_left_subtree, root.len_right_subtree) + 1)
    number_empty_lines = number_lines_with_nodes - 1
    nodes_space = _Y_NODE_SIZE * number_lines_with_nodes
    empty_space = _Y1_START + number_empty_lines * _LINE + _Y1_START  # the last y1 for space in the end

    return nodes_space + empty_space


def _get_x_max():
    count_nodes = len(_keys)
    nodes_space = count_nodes * _X_NODE_SIZE
    empty_space = (count_nodes - 1) * _X_OFFSET

    return _X1_START + nodes_space + empty_space + _X1_START  # the last x1 for space in the end


def _get_tree_keys(root: Node):
    tree_keys = []  # it can be dict with O(1)
    _tree_search(root, tree_keys)

    return tree_keys


def _tree_search(node: Node, tree_keys):
    if node.left:
        _tree_search(node.left, tree_keys)
    tree_keys.append(node.k)
    if node.right:
        _tree_search(node.right, tree_keys)
