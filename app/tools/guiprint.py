from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node
from tkinter import *


_X_INCREMENT = 75
_Y_INCREMENT = 50
_X1_START = 25
_X2_START = 75
_Y_OFFSET = 50  # y2 - y1 may be rename in Y_NODE_SIZE
_SPACE_BETWEEN_ROWS = 2


def guiprint(bt: BinaryTree, parent=None):
    flag = False
    _config_globals()
    if not parent:
        win = Tk()
        flag = True
    else:
        win = Toplevel(parent)
    canvas = Canvas(win, bg='white', width=1000, height=500)
    scroll = Scrollbar(win, command=canvas.yview)
    canvas.config(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, expand=YES, fill=BOTH)
    lines_coordinates = []
    _print_nodes(bt.root, canvas, lines_coordinates)
    _print_lines(canvas, lines_coordinates)
    canvas.config(scrollregion=(0, 0, _x2, _get_y(bt.root)))
    # print((0, 0, _x2, _get_y(bt.root)))
    if flag:
        win.mainloop()


def _config_globals():
    global _x1, _x2, _depth_right_plunge
    _depth_right_plunge = 0
    _x1 = _X1_START
    _x2 = _X2_START


def _print_nodes(node: Node , canvas: Canvas, lines_coord, row=1):
    if node.left:
        _print_nodes(node.left, canvas, lines_coord, row + _SPACE_BETWEEN_ROWS)
    global _x1, _x2, _depth_right_plunge
    # TODO не правильно расчитываю y.
    y1 = (row * _Y_INCREMENT)
    y2 = _Y_OFFSET + (row * _Y_INCREMENT)
    canvas.create_oval(_x1, y1, _x2, y2, fill='green', outline='black')
    canvas.create_text(_x1 + ((_x2 - _x1) / 2),
                        y1 + ((y2 - y1) / 2),
                        text=str(node.k), fill='white')

    if node.left:
        lines_coord.append(_get_own_coord(_x1, y1, _x2, y2))  # itself
    if node.right:
        if node.parent:
            lines_coord.append(_get_own_coord(_x1, y1, _x2, y2))  # itself
            lines_coord.append(_get_child_coordinates(_x1, _x2, row))
            _depth_right_plunge += 1

    _x1 += _X_INCREMENT
    _x2 += _X_INCREMENT
    if node.right:
        _print_nodes(node.right, canvas, lines_coord, row + _SPACE_BETWEEN_ROWS)

    if _depth_right_plunge != 0:  # have all needed coordinates
        _depth_right_plunge -= 1
    else:
        lines_coord.append(_del_x_offset_and_get_coord(_x1, y1, _x2, y2, node))


def _get_y(root: Node):
    number_lines_with_nodes = (max(root.len_left_subtree, root.len_right_subtree) + 1)
    number_empty_lines = number_lines_with_nodes - 1
    nodes_space = _Y_OFFSET * number_lines_with_nodes
    empty_space = _Y_OFFSET + number_empty_lines * _SPACE_BETWEEN_ROWS * _Y_INCREMENT

    return nodes_space + empty_space

def _get_own_coord(x1, y1, x2, y2):
    x = x1 + ((x2 - x1) / 2)
    y = y1 + ((y2 - y1) / 2)

    return x, y


def _del_x_offset_and_get_coord(oldx1, y1, oldx2, y2, node):
    """
    The offset appears when we come back from the right subtree
    The coordinates x1 and x2 take the next position after the
    place where right subtree has its end
    It needs the coordinates of the node (parent mentioned subtree) and
    remove the offset
    """
    x1 = oldx1 - (_X_INCREMENT * (node.len_right_subtree + 1))
    x2 = oldx2 - (_X_INCREMENT * (node.len_right_subtree + 1))
    x = x1 + ((x2 - x1) / 2)
    y = (y1 + ((y2 - y1) / 2))

    return x, y


def _get_child_coordinates(oldx1, oldx2, row):
    x1 = oldx1 + _X_INCREMENT
    x2 = oldx2 + _X_INCREMENT
    x = x1 + ((x2 - x1) / 2)

    y1 = (row + _SPACE_BETWEEN_ROWS) * _Y_INCREMENT
    y2 = _Y_OFFSET + (row + _SPACE_BETWEEN_ROWS) * _Y_INCREMENT
    y = y1 + ((y2 - y1) / 2)

    return x, y


def _print_lines(canvas: Canvas, coordinates: list):
    for i in range(0, len(coordinates), 2):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        id = canvas.create_line(x1, y1, x2, y2, width=3, fill='black')
        canvas.lower(id)
