# Practica 1 
# Bucles

"""valor = float (input("Ingrese un numero: "))

if valor > 0: 
  print ("El numero es positivo")
elif valor == 0:
  print ("Es igual a cero ")
elif valor < 0:
  print ("Es un numero negativo ")
  """
  #While 

""" numero = int (input("Ingrese un numero: "))

for i in range(1, numero +1):
    print (i)

resultado = sum(range(5))

print("Resultado es ", resultado)
"""

 #Ejercicio 3

"""def  sumar_numeros_entre(numero1, numero2) :

  suma = 0
  for numero in range(numero1, numero2 + 1):
   suma += numero
   return suma

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

resultado = sumar_numeros_entre(numero_1, numero_2)

print("La suma entre todos los numeros entre", numero_1, "y", numero_2, "es", resultado)
"""

"""print("Números del 5 al 10")
for i in range(5, 10):
  print(i, end=', ')
# 5, 6, 7, 8, 9,
"""
"""def verificar_credenciales(usuario, contraseña) : 
  usuario_correcto = 'admin'
  clave_correcta = 'admin'

  if usuario == usuario_correcto and contraseña == clave_correcta :
    return True
  else:
    return False
  
usuario = input("Ingrse su usuario: ")
contraseña = input("Ingrese su clave: ")

if verificar_credenciales(usuario, contraseña):
  print("Bienvenido")
else:
  print("Usuario o contraseña incorrecta")  
"""

#Creamos una funcion para verificar los datos, creamos usuario y contraseña
def verificar_credenciales(usuario, contraseña) : 
  usuarios_correctos = {"admin" : "admin", "distameric" : "lasublime"} # Definimos las variables usuario y contraseña, yo lo hice como un diccionario donde primero es le usuario y el segundo valor es la contraseña
  #claves_correctas = ("maracay","soulkidd", "lasublime")

  #Creamos la validación

  if usuario == usuarios_correctos and contraseña == usuarios_correctos:
    return True
  else:
    return False
  
  # Pedimos ingresar el usuario y la contraseña
usuario = input("Ingrse su usuario: ")
contraseña = input("Ingrese su clave: ")

#Hace el proceso de validación, si es true devolvera un mensaje de bienvenida, si es false mostrara que el usuario o la contraseña son incorrectas

if verificar_credenciales(usuario, contraseña):
  print("Bienvenido")
else:
  print("Usuario o contraseña incorrecta")

