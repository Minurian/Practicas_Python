import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
workbook = excel.Workbooks.Open("G:\\Mi unidad\\Copia de invetario fisico3.xlsm")


worksheet = workbook.Worksheets["diacenca"]
print("Seleccionando hoja:", worksheet.name)
print("Rango a seleccionar:", "B1:D45")

try:
    # Método alternativo usando índices
    range_to_select = worksheet.Range("B1:D45")
    range_to_select.Select()
except Exception as e:
    print("Error al seleccionar el rango:", e)