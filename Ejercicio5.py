#Realice el script en Python para una aplicación que permita mediante una 
#estructura while promediar el número de notas definidas por el profesor para 
#un estudiante y determinar si aprueba o no la asignatura. Aprueba con 4,5 en un rango de 0 a 5.0

def promedio_notas(): #calcular el promedio de notas
    print("ingrese el nombre del estudiante")
    print("Ingrese las notas del estudiante (de 0 a 5.0)")
    num_notas = int(input("Número de notas: ")) #numeros de notas, int es para numeros enteros
    suma_notas, contador = 0.0, 0 #suma de notas que el usuario ingrese

    while contador < num_notas: #bucle, se repite hasta que el usuario digita la cantidad de notas que dijo al ini.
        nota = float(input(f"Nota {contador + 1}: ")) # float decimales. muestra el número de la nota que estamos pidiendo nota1, nota2...
        if 0.0 <= nota <= 5.0: #se comprueba si las notas estan en el rango
            suma_notas += nota #suma de notas ingresadas
            contador += 1 #hemos contado una nota más". El contador sube en 1.
        else:
            print("Nota inválida. Intente nuevamente.") #Si la nota no está en el rango el bucle vuelve a pedir 
    
    promedio = suma_notas / num_notas #calcula el promedio dividiendo la suma de las notas por la cantidad de notas
    print("el nombre del estidiante es:")
    print(f"\nPromedio: {promedio:.2f}") #se guarda el resultado en la variable promedio 2f significa que solo mostramos dos números decimales
    print("¡Aprueba!" if promedio >= 4.5 else "No aprueba.")

promedio_notas() # Aquí llamamos a la función que creamos para que empiece a trabajar.
