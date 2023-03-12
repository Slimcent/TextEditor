import tkinter as tk
from tkinter import filedialog


def openfile():
    filename = filedialog.askopenfilename(initialdir="/", title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    print(filename)


form = tk.Tk()
form.title("Python Menus")

menuBar = tk.Menu(form)

#  File menu
fileMenuItems = tk.Menu(menuBar, tearoff=0)
fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Save", command=openfile)
fileMenuItems.add_command(label="Save As", command=openfile)
fileMenuItems.add_command(label="Close", command=openfile)
fileMenuItems.add_separator()  # A seperator
fileMenuItems.add_command(label="Quit", command=form.quit)

menuBar.add_cascade(label="File", menu=fileMenuItems)

#  Edit menu
editMenu = tk.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

menuBar.add_cascade(label="Edit", menu=editMenu)

form.config(menu=menuBar)

textArea = tk.Text(form, height=12, width=80, wrap=tk.WORD)
textArea.pack()

textArea.insert(tk.END, 'Some default text here')
textArea.configure(font=("Arial", 14, "bold", "italic"))

form.mainloop()

