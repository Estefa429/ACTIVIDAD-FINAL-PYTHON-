#Realice el script en Python para una aplicación que permita convertir de dólares a pesos, 
#con una tasa de cambio de $3.934 y mediante una estructura while preguntar si desea seguir realizando
#otras conversiones o no para que de esta manera continue con la ejecución o finalice la aplicación.

def convertir_dolares_pesos(monto_dolares): #def: Se utiliza para definir una función
    valor_conversion = monto_dolares * 3934  # Tasa de conversión fija
    return valor_conversion

# Inicializar variable para controlar el bucle
n = 1

while n == 1:
    # Solicitar monto en dólares
    monto_dolares = float(input("Digite la cantidad de dólares a convertir a pesos: "))
    
    # Realizar conversión
    valor_conversion = convertir_dolares_pesos(monto_dolares)
    print(f"La conversión de {monto_dolares} dólares a pesos es: ${valor_conversion:.2f}")
    
    # Preguntar si desea continuar
    n = int(input("¿Desea realizar otra conversión? Digite 1 para Sí o 2 para no: "))

print("Gracias por usar el convertidor. ¡Hasta luego!")

