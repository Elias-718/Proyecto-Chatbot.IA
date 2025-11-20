trabajador = input("Ingrese el nombre del trabajador:")
sueldo = float(input("Ingrese el sueldo del trabajador:"))
antiguedad = float(input("Ingrese los años de antiguedad:"))

bono = 0.0

if antiguedad >= 20:
    bono = 0.90
    print ("El bono aplicado es:" ,bono)
elif antiguedad >= 10:
    bono = 0.80
    print ("El bono aplicado es:" ,bono)
elif antiguedad >= 5:
    bono = 0.60
    print ("El bono aplicado es:" ,bono)
else:
    print ("No se aplicara ningun bono:")


monto_cobrar = sueldo * bono
descuento = float
descuento = monto_cobrar * 0.05
total_cobrar = monto_cobrar - descuento      



print ("El monto cobrar es:" ,monto_cobrar)
print ("El descuento es:" ,descuento)
print ("El total a cobrar es:" ,total_cobrar)
