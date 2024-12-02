#Desarrolle un programa, que pida al usuario la edad y el sexo, para que la
#computadora le indique si ya puede jubilarse. Tenga en cuenta que un
#Hombre se puede jubilar cuando tenga 63 años en adelante, en cambio, una mujer mayor 
#se jubilará si tiene más de 54 años.

def jubilación():
    # Solicitar datos al usuario
    edad = int(input("Digite su edad: "))
    sexo = input("Digite su sexo (h para hombre, m para mujer): ")

    # Verificar si puede jubilarse según las condiciones
    if sexo == "h":
        if edad >= 63:
            print("Puedes jubilarte.")
        else:
            print("Aún no tienes la edad para jubilarte.")
    elif sexo == "m":
        if edad > 54:
            print("¡Puedes jubilarte!")
        else:
            print("Aún no tienes la edad para jubilarte.")


# Llamar a la función
jubilación()

