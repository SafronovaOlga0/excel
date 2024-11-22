import openpyxl
from openpyxl.chart import LineChart

def chart():
    book=openpyxl.load_workbook("Test.xlsx")
    sheet=book["Коллеги"]

    chart=LineChart()
    chart.add_data("Коллеги!C2:C10")
    chart.title=("Баллы")
    sheet.add_chart(chart)

    book.save("Test.xlsx")