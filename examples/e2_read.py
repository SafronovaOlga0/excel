import openpyxl

def read():
    book = openpyxl.load_workbook("Test.xlsx")
    for row in book["Коллеги"].iter_rows():
        for cell in row:
            print(cell.value)