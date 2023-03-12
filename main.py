import tkinter as tk


def openfile():
    print("File Open")


form = tk.Tk()
form.title("Python Menus")

menuBar = tk.Menu(form)

fileMenuItems = tk.Menu(menuBar, tearoff=0)

fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Save", command=openfile)
fileMenuItems.add_command(label="Save As", command=openfile)
fileMenuItems.add_command(label="Close", command=openfile)
fileMenuItems.add_separator()  # A seperator
fileMenuItems.add_command(label="Quit", command=form.quit)

menuBar.add_cascade(label="File", menu=fileMenuItems)

form.config(menu=menuBar)

form.mainloop()

