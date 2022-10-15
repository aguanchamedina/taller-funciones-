#EJERCICIO N° 3

print("---------------------------------------")
print("-------- DATOS NUMERICOS Y  -----------")
print("------RETOME LA SUMA DE DATOS ---------")
print("---------------------------------------")

def suma_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#INPUT
lista = int(input("Ingrese dato: "))
lista = [1,2,3,4,5,6]
print("La suma es " + str(suma_datos(lista)))

#OUTPUT

#otra manera de hacerlo
#lista1 = [2,3,4,5,6]
#suma = suma_datos(lista1)
#print(suma)
