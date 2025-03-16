import win32com.client
import pyperclip
from PIL import Image
from pywhatkit import sendwhatmsg

#Abrir el excel el libro de trabajo

excel = win32com.client.Dispatch ("Excel.Application")
excel.visible = True
workbook = excel.Workbooks.Open("G:\\Mi unidad\\Copia de invetario fisico3.xlsm")
worksheet = workbook.Worksheets["Hoja1"] 

# Selecciona el rango a capturar
worksheet.Range("A1").Select()

#Copiar el rango a cortapapeles para pegar
excel.Selection.CopyPicture()

#Crea una imagen y pega el inventario al portapapeles

img_data = pyperclip.paste()

#Para guardar la imagen

with open("image.png","wb") as f:
    f.write(bytes(img_data, 'utf-8'))

# Obtener los datos de la imagen del portapapeles
img_data = pyperclip.paste()

# Convertir los datos a formato bytes (asumiendo UTF-8)
img_data_bytes = img_data.encode('utf-8')
# Convertir los datos a formato PIL-Image
img = Image.frombytes('RGB', (1280, 720), img_data_bytes, 'raw')
 # Agrega 'raw' para indicar que los datos son sin procesar

# Guardar la imagen en formato PNG con compresión
img.save("mi_imagen.png", format='PNG', optimize=True)  

excel.quit()

# Define el nombre del archivo con una ruta valida 
nombre_archivo= r"C:\Users\Personal\Downloads\jefferson\Projects"






