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
afp = 1
afp1 = 1/100

n2 = int(input())
fonasa = 1
fonasa1 = 1/100

n3 = int(input())
isapre = 1
isapre1 = 1/100

n4 = int(input())
seguro = 1
seguro1 = 1/100

if opcion == 