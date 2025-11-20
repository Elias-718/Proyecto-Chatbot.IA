nombre = input("Ingrese el nombre del trabajador:")
precio = float(input("Ingrese el precio del producto:"))
cantidad = float(input("Ingrese la cantidad de productos:"))
tipo = input("Ingrese el tipo de producto:") 

monto_pagar = precio * cantidad
descuento = 0.0

if tipo == "regulado":
    descuento = monto_pagar * 0.30
    print ("El producto regulado tiene un descuento del 30%")
elif tipo == "no regulado":
    descuento = monto_pagar * 0.05
    print ("El producto no regulado tiene un descuento del 5%")
elif tipo == "importado":
    descuento = monto_pagar * 0.03
    print ("El producto importado tiene un descuento del 3%")
else:
    print ("No se aplica ningun descuento")

iva = monto_pagar * 0.16
iva = iva - descuento
total_general = monto_pagar + iva
total_general = total_general - descuento

print ("El monto a pagar es:" ,monto_pagar)
print ("El descuento aplicado es:" ,descuento)
print ("El iva es:" ,iva)
print ("El total general es:" ,total_general)


     

