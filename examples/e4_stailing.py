import openpyxl
from openpyxl.styles import Font

def stailing():
    book = openpyxl.load_workbook("Test.xlsx")
    sheet = book["Коллеги"]
    sheet.column_dimensions["A"].width = 100
    sheet.column_dimensions["B"].width = 50

    sheet.column_dimensions["A"].font = Font(size = 24, color='0070C0')

    book.save("Test.xlsx")