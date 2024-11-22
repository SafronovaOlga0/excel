import openpyxl

def formula():
    book=openpyxl.load_workbook("Test.xlsx")
    sheet=book["Коллеги"]
    sheet["E3"]= "=SUM(C2:C5)"
    sheet["E2"]= "AVERAGE(C2:C5)"
    book.save("Test.xlsx")

    
