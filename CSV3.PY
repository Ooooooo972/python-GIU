


import openpyxl
wb = openpyxl.load_workbook("demo.xlsx")
sheet = wb.active
print(sheet.cell(row=1, column=1).value)