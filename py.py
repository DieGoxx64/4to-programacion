opcion = 0
while True:
    print("""
    Dime, ¿Que quieres hacer?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Sacar promedio
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))

        print(" ")
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1 + n2)
    elif opcion == 2:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))

        print(" ")
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1 - n2)
    elif opcion == 3:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))

        print(" ")
        print("RESULTADO: El producto de", n1, "*", n2, "es igual a", n1 * n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primera nota: "))
        n2 = float(input("Introduce tu segunda nota: "))
        n3 = float(input("Introduce tu tercera nota: "))
        q= (n1+n2+n3) / 3
        if q >= 6:
            print("Aprobaste con una excelente nota tu promedio es: ",q)
        elif q >= 4:
            print("Aprobaste apenas con un promedio de: ",q)
        else:
            print("Reprobo con un promedio de: ",q)

    elif opcion == 5:
        break
    else:
        print("Opcion incorrecta")