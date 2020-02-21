try:
    # Python 2
    import Tkinter as tk
    import ttk
    from tkFileDialog import askopenfilename
    import tkMessageBox
except ImportError:
    # Python 3
    import tkinter as tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
    from tkinter import messagebox

import pandas as pd
import openpyxl as opx
import pyexcel
import string
import re
import Excel_Import


# --- classes ---
class MyWindow:

    def __init__(self, parent):

        self.parent = parent

        self.filename = None
        self.df = None
        self.fileTypeFormat = None

        self.text = tk.Text(self.parent)
        self.text.pack()

        self.button = tk.Button(self.parent, text='LOAD DATA', command=self.load)
        self.button.pack()

        self.button = tk.Button(self.parent, text='DISPLAY DATA', command=self.display)
        self.button.pack()


    def convert_xl(self):
        temp_sheet = pyexcel.get_sheet(file_name=self.filename)
        xlsarray = temp_sheet.to_array()

        new_sheet = pyexcel.Sheet(xlsarray)
        new_name = self.filename
        new_name = new_name[:-4]
        new_sheet.save_as(new_name + '_Conv_.xlsx')
 #       self.filename = (new_sheet + '_Conv_.xlsx')

    def memory_address(in_var):
        return hex(id(in_var))

    def load(self):

        name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xlsx', '*.csv')), ('Test', '*.*')])
        self.filename = name
        if name:
            if name.endswith('.csv'):
                self.df = pd.read_csv(name)
                self.fileTypeFormat = 0
            elif name.endswith('.xlsx'):
                self.df = opx.load_workbook(name)
                self.fileTypeFormat = 1
                print(name + ' Has been loaded.')
              #  print (self.memory_address(self.df.dict_object))
                Excel_Import.get_CSV(self.df)
            elif name.endswith('.xls'):
#                self.filename = name
                self.convert_xl()
                print("converting this sheet")
                self.df = opx.load_workbook(name[:-4] + '_Conv_.xlsx')
                print(name[:-4] + '_Conv_.xlsx' + ' Has been loaded.')
                print('Conversion Successful.')
                self.fileTypeFormat = 1
            else:
                try:
                    messagebox.showerror("Error", "File Type Incompatible. Please make sure the file type is either '.xls', '.xlsx' or '.csv'.")
                except ValueError:
                    tkMessageBox.showerror("Error", "File Type Incompatible. Please make sure the file type is either '.xls', '.xlsx' or '.csv'.")

              #  self.df = pd.read_excel(name)
                # self.fileTypeFormat = 1
            self.filename = name

            # display directly
            #self.text.insert('end', str(self.df.head()) + '\n')

    def display(self):
        # ask for file if not loaded yet
        if self.df is None:
            self.load()

        # display if loaded
        if self.df is not None:
            if self.fileTypeFormat == 0:
                self.text.insert('end', self.filename + '\n')
                self.text.insert('end', str(self.df.head()) + '\n')
            elif self.fileTypeFormat == 1:
                sheet = self.df.active
                maxrow = len(sheet['A'])-1
                print(maxrow)
                cells = sheet['A1': 'B{0:0}'.format(maxrow)]
           #     self.d
                count = 0
                for c1, c2 in cells:
                    count = count + 1
                    chars = re.escape(string.punctuation)
                    self.text.insert('end', "{0:0} {1:24} {2:}".format(count, re.sub(r'['+chars+']', ' ', c1.value),re.sub(r'['+chars+']', ' ', c2.value)) + '\n')
                    if count == 15:
                        break
                self.text.insert('end', '\n\n')
              #  print('The Format is XLSX')
            else:
                try:
                    messagebox.showinfo("Error", "File Type incompatible","")
                except ValueError:
                    print("OOPS!")
              #  print("Make Sure this is a correct format!!!")

# --- main ---

if __name__ == '__main__':
    root = tk.Tk()
    top = MyWindow(root)
    root.mainloop()