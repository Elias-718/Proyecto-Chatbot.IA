celsius = input("Ingrese la temperatura:")
c_float = float(celsius) 
fahrenheit = (c_float*9/5) + 32
print ("La temperatura es:" ,fahrenheit)

# Al estarse pidiendo al usuario ingresar datos, no pueden ser un string o un float a la vez asi que se hace
# lo que se hace en la segunda linea que es declarar a la variable celsius como un float mediante otra variable para ingresar datos