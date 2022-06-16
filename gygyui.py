n1 = int(input("ingresa el primer numero : "))
n2 = int(input("ingresa el segundo numero : "))
opcion = 0
while n1 != 0 and n2 != 0:
     print("""
      indique la operacion realizar:
      1) sumar 
      2) restar 
      3) multiplicar 
      4) promedio
      5) cambiar el numero introducido 
      """)
     opcion = int(input("elige una opcion: "))
     if opcion == 1:
         print(" ")
         print(" la suma de", n1 ,"+",n2, "es igual a", n1+n2 )
     elif opcion == 2:
         print(" ")
         print("la resta de",n1,"-",n2,"es igual a", n1-n2 )
     elif opcion == 3:
         print(" ")
         print("el producto de",n1 ,"*",n2 ," es igual a", n1*n2)
     elif opcion == 4:
         print(" ")
         print("tu promedio es", n1+n2//2 )
     elif opcion == 5:






