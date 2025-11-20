#edad = int(input("Ingrese su edad:"))

#if edad <= 12:
    #print ("Eres un niño")
#elif edad <=17:
    #print ("Eres un adolescente")
#elif edad <=64:
    #print ("Eres un adulto")
#elif edad >=65:
    #print ("Eres un anciano")

#color = input("Introduzca el color del semaforo:").lower()

#if color == "verde":
    #print ("Avanzar")
#elif color == "amarillo":
    #print ("Precavido")
#elif color == "rojo":
    #print ("Detenganse")
#else:
    #print ("Color invalido")

monto = float(input("Ingresa el monto total de la compra: "))
tarjeta = input("Tienes tarjeta de fidelidad:").lower()
descuento = 0.0

if monto >= 100 and tarjeta == "si":
    print ("El descuento es del 15%")
elif monto >= 100 and tarjeta == "no":
    descuento = 0.10
    print ("El descuento es del 10%")
elif monto < 100 and tarjeta == "si":
    descuento = 0.05
    print ("El descuento es del 5%")
else:
    print ("Sin ningun descuento")






