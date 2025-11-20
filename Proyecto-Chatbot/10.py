peso = float(input("Ingrese el peso del paquete en kilogramos:"))
zona = input("Ingrese la zona:")

tarifa_nacional = 15
tarifa_internacional = 50
costo_adicional_peso_nacional = 2.50
costo_adicional_peso_internacional = 10

if zona == "nacional":
    costo_total = tarifa_nacional + (peso * costo_adicional_peso_nacional)
    print ("El costo total es:" ,costo_total)
elif zona == "internacional":
    costo_total = tarifa_internacional + (peso * costo_adicional_peso_internacional)
    print ("El costo total es:" ,costo_total)







