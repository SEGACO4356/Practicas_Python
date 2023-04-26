print("Sistema vacacional rappi")

nombre = input("Introduzca el nombre del empleado: ")
clave = int(input("Introduzca la clave de su departamento: "))
antiguedad = float(input("Introduzca los años laborando: "))

if clave == 1:

    if antiguedad >= 1 and antiguedad < 2:
        print("El empleado", nombre, " tiene derecho a 6 días de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print("El empleado", nombre, " tiene derecho a 14 días de vacaciones")
    elif antiguedad >=7:
        print("El empleado", nombre, " tiene derecho a 20 días de vacaciones")
    else:
        print("El empleado", nombre, " aún no tiene derecho a vacaciones")

elif clave == 2:
    if antiguedad >= 1 and antiguedad < 2:
        print("El empleado", nombre, " tiene derecho a 7 días de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print("El empleado", nombre, " tiene derecho a 15 días de vacaciones")
    elif antiguedad >=7:
        print("El empleado", nombre, " tiene derecho a 22' días de vacaciones")
    else:
        print("El empleado", nombre, " aún no tiene derecho a vacaciones")



elif clave == 3:
    if antiguedad >= 1 and antiguedad < 2:
        print("El empleado", nombre, " tiene derecho a 10 días de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print("El empleado", nombre, " tiene derecho a 20 días de vacaciones")
    elif antiguedad >=7:
        print("El empleado", nombre, " tiene derecho a 30 días de vacaciones")
    else:
        print("El empleado", nombre, " aún no tiene derecho a vacaciones")



else:
    print("La clave no existe.")


