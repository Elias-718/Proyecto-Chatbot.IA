calificacion = int(input("Ingrese una calificacion:"))

if calificacion >= 90:
    print ("Excelente")
elif calificacion >= 80 or calificacion <90 :
    print ("Buen trabajo")
elif calificacion >= 70 or calificacion <80:
    print ("Aprobado")
elif calificacion >= 60 or calificacion <= 70:
    print ("Mejorable")
elif calificacion >= 60:
    print ("Reprobado")

    