#Un aprendiz desea saber cuál será su calificación final en cierta asignatura. 
#Las notas que se manejan son de 0 a 5.
#	30% el primer examen.
#	30% el segundo examen
#	40% el último examen
#Pedir al usuario nombre, asignatura, las 3 notas de los exámenes y determinar la calificación 
#definitiva teniendo en cuenta los porcentajes dados. Además, para que el aprendiz apruebe su
#calificación final debe ser mayor o igual a 4.0

def notas_asignatura():
    # Solicitar datos al usuario
    nombre = input("Digite su nombre: ")
    asignatura = input("Digite su asignatura: ")
    print("Por favor, ingrese las notas de los exámenes (de 0 a 5):")

    # Ingresar las notas de los exámenes
    nota1 = float(input("Digite la primera nota: "))
    nota2 = float(input("Digite la segunda nota: "))
    nota3 = float(input("Digite la tercera nota: "))

    # Calcular la calificación final
    calificacion_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

    # Verificar si el estudiante aprueba
    if calificacion_final >= 4.0:
        print(f"Has aprobado la asignatura {asignatura} con una calificación de {calificacion_final:.2f}.")
    else:
        print(f"{nombre}, no has aprobado la asignatura {asignatura}. Tu calificación final es {calificacion_final:.2f}.")

# Llamada a la función
notas_asignatura()





