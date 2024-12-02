#Realice el script en Python para una aplicación que permita a 
#partir de un número que digite el usuario por teclado 
#(número entero n), calcular su factorial (n!).

def calcular_factorial(n): #def declara la función llamada calcular_factorial (n es el numero del cual se va a calcular)
    return 1 if n == 0 else n * calcular_factorial(n - 1) #Verifica si n es igual a 0. si es verdad res. 1
                                                          #n * por el resueltado llamndo la función on el número decrementado en uno (n-1).
n = int(input("Ingrese un número entero no negativo: "))
if n < 0:
    print("El número no debe ser negativo.")
else:
    print(f"El factorial de {n} es: {calcular_factorial(n)}") #F permite incluir valores de variables dentro del texto.
                                                              #Llama la función calcular_factorial

