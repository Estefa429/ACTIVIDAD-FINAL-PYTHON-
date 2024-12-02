#Realice  el script en Python para una aplicación que permita preguntarle al
#usuario una cantidad de dinero a invertir, el interés anual y el sistema
#muestre por pantalla el capital obtenido en la inversión.

# Función para calcular el capital final con interés compuesto
def calcular_inversion(capital_inicial, interes_anual, tiempo):
    capital_final = capital_inicial * (1 + interes_anual) ** tiempo
    return capital_final

# Solicitar los datos al usuario
capital_inicial = float(input("Introduce la cantidad de dinero a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): ")) / 100  # Convertir porcentaje a decimal
tiempo = float(input("Introduce el tiempo de la inversión en años: "))

# Calcular el capital final
capital_final = calcular_inversion(capital_inicial, interes_anual, tiempo)

# Mostrar el resultado
print(f"El capital obtenido después de {tiempo} años será: ${capital_final:.2f}")