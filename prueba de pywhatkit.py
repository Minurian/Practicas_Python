import pywhatkit 
import openpyxl

# Ruta absoluta: Sirve para que el programa busque el archivo especificamente donde esta copiando la direccion raiz

file_path = "G:\\Mi unidad\\Copia de invetario fisico3.xlsm"

#Abre el archivo de excel y el data_only=true es para que muestre la informacion correcta y no las formulas en caso de haber formulas en las celdas a seleccionar
workbook = openpyxl.load_workbook(file_path, data_only=True)

#Selecciona la hoja a trabajar

sheet = workbook ['NOVIEMBRE']


#sheet_names = workbook.sheetnames

#print(sheet_names)

#Obtener una hoja especifica



#Acceder a una celda e imprimir su valor

cell_value = sheet['C192'].value
mensajes_bytes = str(cell_value).encode("utf-8")
print(cell_value)

#informacion = (cell_value)


pywhatkit.sendwhatmsg_instantly("+584126350266", mensajes_bytes)






#range_cells = sheet['A2':'B5']

#saludo = input("")

#pywhatkit.sendwhatmsg_instantly("+584126350266", saludo)

