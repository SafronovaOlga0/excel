import openpyxl
import openpyxl.workbook

def update():
    book = openpyxl.load_workbook("Test.xlsx")
    sheet = book["Коллеги"]
    sheet.insert_rows(1)
    sheet['A1'].value = "ФИО"
    sheet['B1'].value = "Телефон"
    sheet['C1'].value = "Баллы"
    sheet['D1'].value = "Посты"

    sheet.delete_rows(2)

    book.save("Test.xlsx")


