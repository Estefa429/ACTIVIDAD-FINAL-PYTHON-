#Realice el script en Python para una aplicación que permita mostrar en pantalla los números del 1 al 30
#escribiendo un salto de línea cada 7 números. Salto de Línea = \n

def mostrar_numeros(num): #def: Se utiliza para definir una función(mostrar_numeros es el nombre)(num es el limite
                            #hasta el numero que se imprime)
    for i in range(1, num + 1): #range Genera una secuencia de números desde 1 hasta num
        print(i, end=" ")
        if i % 7 == 0: #i % 7: Calcula el residuo de dividir i entre 7
            print()  #print no tiene argumentos, por lo que genera un salto de línea,


mostrar_numeros(30) #Llama a la función mostrar_numeros, pasando 30 como argumento.





def salto_linea(): #def: Se utiliza para definir una función(mostrar_numeros es el nombre)(num es el limite
                            #hasta el numero que se imprime)
    for i in range(1, 31): #range Genera una secuencia de números desde 1 hasta num
        print(i, end=" ")
        if i % 7 == 0: #i % 7: Calcula el residuo de dividir i entre 7
            print("\n", end="")  #print no tiene argumentos, por lo que genera un salto de línea,
        print()

salto_linea() #Llama a la función mostrar_numeros, pasando 30 como argumento.




