from app.binary_tree.BinaryTree import BinaryTree
from app.binary_tree.Node import Node
from tkinter import *
from app.tools.GetterSubtreeLens import GetterSubtreeLens


def guiprint(bt: BinaryTree, parent=None):
    flag = False
    global _list_subtree_lens, _x1, _x2, _cur_index
    _x1 = 25
    _x2 = 75
    _cur_index = 0
    _list_subtree_lens = GetterSubtreeLens(bt).get()
    if not parent:
        win = Tk()
        flag = True
    else:
        win = Toplevel(parent)
    canvas = Canvas(win, bg='white', width=1000, height=500)
    canvas.pack()
    arr = []
    _f(bt.root, canvas, arr)
    _ff(canvas, arr)
    if flag: win.mainloop()


def _f(node: Node , canvas: Canvas, arr, depth=1):
    if node.left:
        _f(node.left, canvas, arr, depth + 2)
    global _x1, _x2, _cur_index
    y1 = (depth * 50)
    y2 = 50 + (depth * 50)
    canvas.create_oval(_x1, y1, _x2, y2, fill='green', outline='black')
    canvas.create_text(_x1 + 25, y1 + 25, text=str(node.k), fill='white')
    if node.left:
        arr.append((_x1, y2))
    if node.right:
        arr.append((_x2, y2))
    _x1 += 75
    _x2 += 75
    if node.right:
        _cur_index += 1
        _f(node.right, canvas, arr, depth + 2)
        _cur_index -= 2
# [[0, 0], [1, 1], [0, 0], [2, 2], [0, 0], [1, 1], [0,0]]
    if node.parent:
        if node == node.parent.left:
            id = _list_subtree_lens[_cur_index][0] + 1
            arr.append((_x2 - (75 * id), y1))
        else:
            id = _list_subtree_lens[_cur_index][1] + 1
            arr.append((_x1 - (75 * id), y1))
    _cur_index += 1


def _ff(canvas: Canvas, arr):
    pass
    # for i in range(0, len(arr), 2):
    #     x1, y1 = arr[i]
    #     x2, y2 = arr[i + 1]
    #     canvas.create_line(x1, y1, x2, y2, width=3, fill='black')



