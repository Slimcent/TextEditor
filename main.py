import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

filename = ''


def close_file():
    textArea.delete('1.0', tk.END)


def save_file_as():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if save_text_as:
        text_to_save = textArea.get('1.0', 'end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error", "Cancelled")


def savefile():
    global filename
    if filename:
        text_area_text = textArea.get('1.0', 'end-1c')
        save_text = open(filename, 'w')
        save_text.write(text_area_text)
        save_text.close()
    else:
        messagebox.showinfo("Error", "No file open")


def openfile():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    try:
        if filename:
            the_file = open(filename)
            textArea.delete('1.0', tk.END)
            textArea.insert(tk.END, the_file.read())
            the_file.close()
        elif not filename:
            messagebox.showinfo("Cancel", "You clicked Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")


def openfile1():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    textArea.delete('1.0', tk.END)
    try:
        if filename:
            the_file = open(filename)
            for line in the_file.readlines():
                text_line = parseline(line)
                textArea.insert(tk.END, text_line + '\n')

            the_file.close()
        elif not filename:
            messagebox.showinfo("Cancel", "You clicked Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")


def parseline(the_line):
    parsed_line = the_line.strip()
    space_pos = parsed_line.rfind(' ')
    new_text_line = parsed_line[space_pos:] + ", " + parsed_line[:space_pos]
    return new_text_line.strip()


form = tk.Tk()
form.title("Python Menus")

menuBar = tk.Menu(form)

#  File menu
fileMenuItems = tk.Menu(menuBar, tearoff=0)
fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Open1", command=openfile1)
fileMenuItems.add_command(label="Save", command=savefile)
fileMenuItems.add_command(label="Save As", command=save_file_as)
fileMenuItems.add_command(label="Clear", command=close_file)
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

textArea = tk.Text(form, height=12, width=80, wrap=tk.NONE)
textArea.insert(tk.END, 'Some default text here')
textArea.configure(font=("Arial", 11))

scrollV = tk.Scrollbar(form, orient=tk.VERTICAL)  # Vertical scroll bar
scrollV.config(command=textArea.yview)
textArea.configure(yscrollcommand=scrollV.set)
scrollV.pack(side=tk.RIGHT, fill=tk.Y)

scrollH = tk.Scrollbar(form, orient=tk.HORIZONTAL)  # Horizontal scroll bar
scrollH.config(command=textArea.xview)
textArea.configure(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)

textArea.pack()
form.mainloop()
