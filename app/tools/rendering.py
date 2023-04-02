import os
from tkinter import *
from tkinter.colorchooser import askcolor
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.pgprint import pgprint
from app.tools.guiprint import guiprint


def render(bt: BinaryTree):
    root = Tk()
    root.title('Pretty graph print')
    root.resizable(False, False)
    _place_window(root, 500, 350)
    root.config(bg='white')

    font = ('Roman', 15, 'normal')
    Label(root, text='Please, choose how to render the graph',
          font=font, bg='#6bceff', pady=10).pack(fill=X)

    canvas = Canvas(width=500, height=300, bg='#d1d6e0')
    canvas.pack(expand=YES, fill=BOTH)

    img_path = os.path.abspath('../images/console_rendering.png')
    img = PhotoImage(file=img_path, width=150, height=150)
    widget = Button(canvas, image=img, bd=5, relief=RAISED,
                    command=lambda: pgprint(bt))
    widget.pack()
    canvas.create_window(150, 125, window=widget)

    font = ('times', 15, 'normal')
    canvas.create_text(150, 250, text='Console', font=font)
    canvas.create_text(350, 250, text='GUI', font=font)

    img_path2 = os.path.abspath('../images/image.png')
    img2 = PhotoImage(file=img_path2, width=150, height=150)
    widget2 = Button(canvas, image=img2, bd=5, relief=RAISED,
                     command=lambda: guiprint(bt))
    widget2.pack()
    canvas.create_window(350, 125, window=widget2)

    root.mainloop()


def _place_window(win: Tk, win_width, win_height):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x_cordinate = int((screen_w / 2) - (win_width / 2))
    y_cordinate = int((screen_h / 2) - (win_height / 2))
    win.geometry("{}x{}+{}+{}".format(win_width, win_height, x_cordinate, y_cordinate))