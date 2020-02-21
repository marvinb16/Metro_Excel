import openpyxl
import pandas as pd
import string
import re


def get_CSV(obj):
    data = obj
    sheet = data.active
    maxrow = len(sheet['A']) - 1
    print(maxrow)
    cells = sheet['A1': 'B{0:0}'.format(maxrow)]
    #     self.d
    count = 0
    for c1, c2 in cells:
        count = count + 1
        chars = re.escape(string.punctuation)
        print("{0:0} {1:24} {2:}".format(count, re.sub(r'[' + chars + ']', ' ', c1.value),
                                                           re.sub(r'[' + chars + ']', ' ', c2.value)) + '\n')
        if count == 15:
            break
   # print('end', '\n\n')
    print("Address at: ")
    print(data)
    return