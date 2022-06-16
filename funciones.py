
def puntuación(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuación(clase)
print("la puntuación de esta clase es:", media)

clase = [5, 6, 7.5, 10]
media = puntuación(clase)
print("la puntuación de esta clase es:", media)