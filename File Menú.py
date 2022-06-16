def main():
    print("Nintendo Eshop")

    objetivo = float(input("¿Cuántos fondos quieres añadir: "))

    añadir = 50
    while objetivo > añadir:
        añadir += float(input("¿Cuántos fondos quieres añadir a tu cuenta? "))

    print(f"¡objetivo conseguido! usted a añadido { añadido} 50 dolares. ")
