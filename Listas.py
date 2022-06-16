# definir una lista de tipo str
nombres = ["juan","karla","ricardo","maria"]
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# imprimir un rago
print(nombres[0:2]) #sin incluir el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])
# cambias un valor
nombres[3] = "Ivone"
print(nombres)
# iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existe más nombres en la lista")
# preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append("lorenzo")
print(nombres)
# insertar un elemento en un indice en especifico
nombres.insert(1, "Octavio")
print(nombres)
# remover un elemento
nombres.remove("Octavio")
print(nombres)
# remover el ultimo valor agregado
nombres.pop()
print(nombres)
# eliminar un indice
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print("nombres")