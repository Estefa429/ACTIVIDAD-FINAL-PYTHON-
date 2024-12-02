# Realice el script en Python para una aplicación que permita 
# imprimir los números impares, según el rango de datos determinado por el usuario

def imprimir_impares(a, b): #def: Declara una nueva función llamada imprimir_impares.
    for numero in range(a, b +1): #for bucle finito (numero es la variable) (range Genera una secuencia de números que comienza en a)
        if numero % 2 !=0: #Calcula el residuo de la división de numero entre 2. (!= Distinto o igual)
                            #!= 0: Comprueba si el residuo no es 0, lo cual indica que el número es impar.
            print(numero)

a = int(input("Digite el primer numero del rango: "))
b = int(input("Digite el segundo numero del rango: "))

if a > b :
    print("El numero b debe ser mayor al numero a")
else:
    imprimir_impares(a,b)



