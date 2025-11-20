my_lista = list()
my_other_lista = [] #list() o [] es lo mismo

print (len(my_lista))

my_lista = [35, 18, 62, 32, 34, 34, 36]

print (my_lista)
print (len(my_lista))

my_other_lista = [18, 1.70, "Elias", "Romero"]

print (type(my_other_lista))
print (type(my_lista))

print (my_other_lista+my_lista) # Aqui concatenas o unes dos listas con todos sus elementos
print (len(my_other_lista+my_lista)) # Aqui concatenas o unes dos listas con todos sus elementos
#print (my_other_lista-my_lista) Error y con el * o / sera igual


print (my_other_lista[0])
print (my_other_lista[1])
print (my_other_lista[2])
print (my_other_lista[3])
print (my_other_lista[-1])
print (my_other_lista[-2])
print (my_other_lista[-3])
print (my_other_lista[-4])
print (my_lista.count(34)) # Va a contar la misma cantidad de veces que se repite un valor

#print (my_other_lista[4]) Da error ya que no hay un cuarto elemento en la lista my_other_list
#print (my_other_lista[-5]) IndexError: list index out of range

edad, altura, nombre, apellido = my_other_lista
print (nombre) # Ejecutara el elemento en la posicion que se encuentre my_other_lista, si ponemos nombre, ejecutara Elias o pones apellido ejecutara Romero

nombre, edad, apellido, altura = my_other_lista[2], my_other_lista[0], my_other_lista[3], my_other_lista[1]
print (edad) # Este comparado con el anterior es mas largo, redudante, mas dificil de ver visualmente y si te equivocas poniendo el numero, dara error

my_other_lista.append("Tortosa") # append lo que hara sera añadir un nuevo elemento al final de la lista
print (my_other_lista)

my_other_lista.insert(1, "Guau") # insert inserta un nuevo elemento antes del primero osea corre el primero y se coloca el nuevo elemento
print (my_other_lista)

my_other_lista[1] = "Rojo"
print (my_other_lista)

my_other_lista.remove(18) # remove elimina lo que pongas de elemento en el parentesis
print (my_other_lista)

my_lista.remove(34)
print (my_lista)

print(my_lista.pop()) # pop elimina el ultimo elemento pero a su vez lo regresa (fuera de la lista)
print (my_lista)


my_pop_elemento = my_lista.pop(2)
print(my_pop_elemento)
print (my_lista)

del my_lista[2] # A diferencia del remove que elimina el nombre del elemento, el del elimina por orden en el que hayas puesto
print(my_lista)

my_new_lista = my_lista.copy() # Aqui se crea una nueva variable que es igual a my_lista antes del clear
print (my_new_lista)

my_lista.clear()
print (my_lista)
print (my_new_lista)

my_new_lista.reverse() # Revierte el orden de los elementos
print (my_new_lista)

my_new_lista.sort() # Ordena de menor a mayor
print (my_new_lista)

print (my_new_lista[1:4])




my_lista = "Hola Python"
print (my_lista) 
print (type(my_lista)) 





