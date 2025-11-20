antiguedad = int(input("Ingrese los años de antiguedad:"))
desempeño = input("Ingrese su nivel de desempeño:")

sueldo_base = 1500.00

if antiguedad >= 5:
    if desempeño == "A":
        porcentaje_bono = 0.20
    elif desempeño == "B":
        porcentaje_bono = 0.10
    elif desempeño == "C":
        porcentaje_bono = 0.05

if antiguedad < 5:
    if desempeño == "A":
        porcentaje_bono = 0.15
    elif desempeño == "B":
        porcentaje_bono = 0.07
    elif desempeño == "C":
        porcentaje_bono == 0.02

monto_bono = sueldo_base * porcentaje_bono
sueldo_total = sueldo_base + monto_bono

print ("El monto del bono es:" ,monto_bono)
print ("El sueldo total es:" ,sueldo_total)
    


    

    
    

