#EJERCICIO N° 2

print("---------------------------------------")
print("-------- CADENA DE PARAMETROS ---------")
print("----------- MOSTRADO N VECES ----------")
print("---------------------------------------")

def mostrar_cadena(cadena, n):
    for i in range(n):
        print(cadena)

#INPUT
cadena1 = input("Digite una cadena de texto: ")
n1 = int(input("Digite el numero de veces a mostrar la cadena: "))
mostrar_cadena(cadena1 , n1)

#OUTPUT
