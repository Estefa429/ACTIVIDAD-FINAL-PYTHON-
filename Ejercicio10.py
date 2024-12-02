#En un almacén se descuenta 20% del precio al cliente si el valor a pagar es mayor a $20.000. 
#Dado un valor de precio, muestre lo que debe pagar el cliente.

def val(valor,valor_descuento):
    if valor >= 20000:
        print("el valor a pagar es de:" , (valor - valor_descuento))

    else:
        valor < 20000
        print("el valor a pagar es" , valor)

valor = int(input("Digite el precio:"))
valor_descuento = valor * 0.20

val(valor, valor_descuento)