while True:
    print("1 = suma")
    print("2 = resta")
    print("3 = multiplicacion")
    print("4 = divicion")
    print("5 = promedio (3 notas)")
    print("6 = salir")
    op=int(input("INGRESE OPCION"))

    if op == 1 :
        num1=int(input("ingrese primer numero"))
        num2=int(input("ingrese segundo numero"))
        sum=num1+num2
        print("tu resultado de la suma es: ", sum)
        print("1 = volver a hacer la suma")
        print("2 = volver al menu")
        op2=int(input("ELIGE OPCION"))
        if op2 == 1 :
            num1 = int(input("ingrese primer numero"))
            num2 = int(input("ingrese segundo numero"))
            sum = num1 + num2
            print("tu resultado de la suma es: ", sum)
            print("1 = volver a hacer la suma")
            print("2 = volver al menu")
            op2 = int(input("ELIGE OPCION"))
    elif op == 2 :
        num1 = int(input("ingrese primer numero"))
        num2 = int(input("ingrese segundo numero"))
        res = num1 - num2
        print("tu resultado de la suma es: ", res)
        print("1 = volver a hacer la resta")
        print("2 = volver al menu")
        op2 = int(input("ELIGE OPCION"))
        if op2 == 1 :
            num1 = int(input("ingrese primer numero"))
            num2 = int(input("ingrese segundo numero"))
            res = num1 - num2
            print("tu resultado de la suma es: ", res)
            print("1 = volver a hacer la resta")
            print("2 = volver al menu")
            op2 = int(input("ELIGE OPCION"))
    elif op == 3 :
        num1 = int(input("ingrese primer numero"))
        num2 = int(input("ingrese segundo numero"))
        mul = num1 * num2
        print("tu resultado de la multiplicacion es: ", mul)
        print("1 = volver a hacer la multiplicacion")
        print("2 = volver al menu")
        op2 = int(input("ELIGE OPCION"))
        if op2 == 1 :
            num1 = int(input("ingrese primer numero"))
            num2 = int(input("ingrese segundo numero"))
            mul = num1 * num2
            print("tu resultado de la multiplicacion es: ", mul)
            print("1 = volver a hacer la multiplicacion")
            print("2 = volver al menu")
            op2 = int(input("ELIGE OPCION"))
    elif op == 4 :
        num1 = int(input("ingrese primer numero"))
        num2 = int(input("ingrese segundo numero"))
        div = num1 / num2
        print("tu resultado de la suma es: ", div)
        print("1 = volver a hacer la divicion")
        print("2 = volver al menu")
        op2 = int(input("ELIGE OPCION"))
        if op2 == 1 :
            num1 = int(input("ingrese primer numero"))
            num2 = int(input("ingrese segundo numero"))
            div = num1 / num2
            print("tu resultado de la suma es: ", div)
            print("1 = volver a hacer la divicion")
            print("2 = volver al menu")
            op2 = int(input("ELIGE OPCION"))
    elif op == 5 :
        num1 = int(input("ingrese primera nota"))
        num2 = int(input("ingrese segunda nota"))
        num3 = int(input("ingrese tercera nota"))
        prom = (num1 + num2 + num3)/3
        print("tu resultado de la suma es: ", prom)
        print("1 = volver a hacer el promedio")
        print("2 = volver al menu")
        op2 = int(input("ELIGE OPCION"))
        if op2 == 1 :
            num1 = int(input("ingrese primera nota"))
            num2 = int(input("ingrese segunda nota"))
            num3 = int(input("ingrese tercera nota"))
            prom = (num1 + num2 + num3) / 3
            print("tu resultado de la suma es: ", prom)
            print("1 = volver a hacer el promedio")
            print("2 = volver al menu")
            op2 = int(input("ELIGE OPCION"))


    elif op == 6 :
        print("USTED A SALIDO DEL PROGRAMA")
        break
