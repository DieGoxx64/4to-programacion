print("CONFIRME SU CONTRASEÑA")
password_1 = input("escriba su contraseña: ")
password_2 = input("escriba de nuevo su contraseña: ")

while password_1 != password_2:
    print("las contraseñas no coinciden. intentalo de nuevo.")
    password_1 = input("escriba su contraseña: ")
    password_2 = input("escriba de nuevo su contraseña: ")

    print("contraseña confirmada. ¡Hasta la vista! ")
