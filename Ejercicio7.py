#Escribir un algoritmo que, ingrese los siguientes datos:
#	Nombre del aprendiz
#	Asignatura
#	Calificación final.
#Tener en cuenta que las calificaciones serán del 1 al 10, y se debe mostrar en pantalla:
#	Cuando la calificación sea menor de 7, mostrar el mensaje de «REPROBADO»
#	Cuando la calificación sea de 7 o superior mostrar el mensaje de «APROBADO»

def datos(): #def: Se utiliza para definir una función
    Nombre_aprendiz = input("Digite el nombre: ")
    Asignatura = input("Digite el asignatura: ")
    Calificación = float(input("Digite la calificación final: "))

    if Calificación < 7:
        print("REPROBADO")

    elif Calificación >= 7:
        print("APROBADO")
    
# Llamar a la función
datos()