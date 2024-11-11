ItemsHorizonte = 5 

inventario = int (input ("Ingrese la cantidad del inventario "))

print("tienes un total de " , inventario)

Valor1 = int (input("Ingrese la cantidad que desea distribuir "))

if Valor1 > inventario: 
    print ("La cantidad ingresada sobre pasa el inventario ")
else :
    cantidad_por_tipo = Valor1 // ItemsHorizonte
    resto = valor1 % ItemsHorizonte

    print ("Debes colocar por tipo: " , cantidad_por_tipo)

    if resto > 0:
        for i in range (resto): 
            cantidad_por_tipo += 1
            print

#resultado = inventario/Valor1

#print ("Debes colocar por tipo " , resultado)

#El resultado debe tener en cuenta que existen 5 tipos de producto y que debe ser distribuido  en base a lo que se pidio entre lo que se tiene en inventario  