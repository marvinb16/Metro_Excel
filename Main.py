from tkinter import *

root = Tk()
root.title('PSS Excel Reformat')

root.geometry("500x500")
root.resizable(0, 0)

menu = Menu(root)
root.config(menu=menu)
# DropDown menu Config
# menuname = Menu("the frame", tearoff=0
# menu.add_cascade(label, menu=^^)
# men

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Load File's")
subMenu.add_command(label="Format Setting")
subMenu.add_command(label="Settings")
subMenu.add_separator()
subMenu.add_command(label="Exit")

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Label")

# toolbar :)
#toolbar = Frame(root, bg="blue")

#readTemp = Button(toolbar, text="Temp")
#readTemp.pack(side=LEFT, padx=6, pady=6)
#readHud  = Button(toolbar, text="Humidity")
#readHud.pack(side=LEFT, padx=2, pady=2)

#toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text="Label", bd=2, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# graphics

root.mainloop()