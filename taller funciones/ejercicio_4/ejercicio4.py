#EJERCICIO N° 4

print("----------------------------------")
print("--------PROMEDIO DE DATOS---------")
print("----------------------------------")

def promediar(lista):
    suma = 0
    promedio = 0 
    cont = 0 
    for i in lista:
        suma = suma + i
        cont = cont + 1
    promedio = suma / cont 
    return promedio

#INPUT
lista1 = [2,3,4,5,6]
promedio = promediar(lista1)
print(promediar)
#OUTPUT
