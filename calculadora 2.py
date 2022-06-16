opcion = 1
while opcion != 5:
    print("introduce una opcion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input())
    print("Introduce el primer número")
    n1 = int(input())
    print("Introduce el segundo número")
    n2 = int(input())
    if opcion == 1:
        suma = n1+n2
        print(str(suma))
    elif opcion == 2:
        resta = n1-n2
        print(str(resta))
    elif opcion == 3:
        multiplicacion = n1+n2
        print(str(multiplicacion))
    elif opcion == 4:
        division = n1/n2
        print(str(division))
    elif opcion == 5:
        print("Terminando")
