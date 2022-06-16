print("sistema de sueldo liquido")
nombre= input("ingrese su nombre:")
afp = int(input("ingrese cuanto le descuentan por afp: "))
prevision=input("ingrese si es Fonasa o Isapre: ")
previsionPorc=int(input(f"ingrese cuanto le descuentan en {prevision}: "))
seguro=int(input("ingrese cuanto le descuentan en el seguro de cesantia: "))

opcion = 1
while opcion!= 3:
    print("introduce una opcion")
    print("1. calcular sueldo imponible")
    print("2. calcular los descuentos")
    print("3. salir")
    opcion = int(input())
n1 = int(input())
afp = 2
afp1 = 2/100

n2 = int(input())
fonasa = 4
fonasa1 = 4/100

n3 = int(input())
isapre = 1
isapre1 = 1/100

n4 = int(input())
seguro = 3
seguro1 = 3/100

if opcion == 2:
    suma = n1
    print(str(suma))

elif opcion == 4:
     resta = n2
     print(str(resta))

elif opcion == 1:
     dividir = n3
     print(str(dividir))

elif opcion == 3:
     multiplicar = n4
     print(str(multiplicar))

elif opcion == 1:
     print("¿Cual prefieres?")

