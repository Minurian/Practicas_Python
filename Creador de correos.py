import win32com.client as win32

#Crea una instancia con outlook

outlook = win32.Dispatch("Outlook.Application")
mail =outlook.CreateItem(0)

#Configurando el Mensaje

mail.to = "Jeffersoonpaez@gmail.com"
mail.subject = "Prueba para el correo"
mail.body = "Este es un correo enviado desde python"

#Enviar mensaje 

mail.send()