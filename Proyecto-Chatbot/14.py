#edad = int(input("Ingrese su edad:"))

#if edad < 0 or edad > 120:
    #print ("Edad no valida")
#elif edad >= 18:
    #print ("Puedes votar")
#else:
    #print ("No puedes votar")

#contraseña = input("Ingrese una contraseña:")

#if len(contraseña) >=8:
    #print ("Contraseña fuerte")
#else:
    #print ("Contraseña debil")

#dia = input("Ingresa un dia de la semana:").lower()
#if dia == "sabado" or "domingo":
    #print ("Es fin de semana!")
#else:
    #print ("Es un dia de semana")

#caracter = input("Ingresa un caracter: (preferiblemente un simbolo)")

#if caracter == "$" or caracter == "%" or caracter == "#":
    #print ("Intenta con otro")
#else:
    #print ("Caracter aprobado")

edad = int(input("Ingresa tu edad: "))
pase = input("Tienes pase especial:").lower()

if edad > 60 or pase == "si":
    print ("Acceso prioritario")
else:
    print ("Acceso normal")




