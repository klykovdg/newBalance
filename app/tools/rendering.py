import os
from tkinter import *
from tkinter.messagebox import showerror
from app.binary_tree.BinaryTree import BinaryTree
from app.tools.pgprint import pgprint


def render(bt: BinaryTree):
    root = Tk()
    root.title('Pretty graph print')
    root.config(bg='white', width=500, height=500)

    font = ('Roman', 15, 'normal')
    Label(root, text='Please, choose how to render the graph',
          font=font, bg='#00CCFF', pady=10).pack(fill=X)
    canvas = Canvas(width=500, height=300, bg='white')
    canvas.pack(expand=YES, fill=BOTH)

    img_path = os.path.abspath('../images/console.png')
    img = PhotoImage(file=img_path, width=150, height=150)

    widget = Button(canvas, image=img, bd=5, relief=RAISED,
                    command=lambda: pgprint(bt))
    widget.pack()
    canvas.create_window(150, 150, window=widget)

    font = ('times', 15, 'normal')
    canvas.create_text(150, 250, text='Console', font=font)
    canvas.create_text(350, 250, text='GUI', font=font)

    widget2 = Button(canvas, image=img, bd=5, relief=RAISED,
                     command=lambda: showerror('Error', 'Not yet implemented'))
    widget2.pack()
    canvas.create_window(350, 150, window=widget2)

    root.mainloop()