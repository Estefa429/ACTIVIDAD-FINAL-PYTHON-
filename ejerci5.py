def main(): #def declara la función llamada  main
    nombre = input("Nombre del estudiante: ")##input para pedir el dato la variable es llamada nom
    grado = input("Grado del estudiante: ")
    numero_notas = int(input("Número de notas: "))
    
    notas = [] #para guardar las notas lista vacia
    i = 0 #cantidad de notas
    while i < numero_notas: # Un bucle es como un ciclo que repite algo varias veces
        try: #estructura de manejo de errores
            nota = float(input(f"Ingrese la nota {i + 1} (0 a 5.0): ")) #numero de notas
            if 0 <= nota <= 5.0:
                notas.append(nota)#notas es una lista - agrega un nuevo elemento 
                i += 1 #manera abreviada de i = i+1
            else:
                print("Nota fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    
    promedio = sum(notas) / numero_notas #definido por phyton
    estado = "aprueba" if promedio >= 4.5 else "no aprueba"
    
    print(f"\nEstudiante: {nombre}\nGrado: {grado}\nPromedio: {promedio:.2f}\nEstado: {estado}")

if __name__ == "__main__": #le dice a Python que solo ejecute la función main() #es para decile al bloque que se ejecute 
    main() #llama la función

