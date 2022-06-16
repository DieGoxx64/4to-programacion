def escribirSubrayado(texto):
    print(texto)
    for i in range(0, len(texto)):
        print("-", end="")
    print()

escribirSubrayado ("Primer ejemplo")
escribirSubrayado ("Segundo ejemplo")
escribirSubrayado ("Tercer ejemplo")