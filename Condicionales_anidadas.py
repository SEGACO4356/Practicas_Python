print("Conversor")

print("Menu de opciones")

print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número")

opcion = int(input("Cual es su opción deseada?"))

if opcion == 1:
    print("De número a palabra")

    opcion_1 = int (input("Cual es el número a convertir? "))

    if opcion_1 == 1:
        print("Uno")
    elif opcion_1 == 2:
        print("Dos")
    elif opcion_1 == 3:
        print("Tres")
    elif opcion_1 == 4:
        print("Cuatro")
    elif opcion_1 == 5:
        print("Cinco")
    elif opcion_1 == 6:
        print("Seis")
    elif opcion_1 == 7:
        print("Siete")
    else:
        print("No está registrado")
elif opcion == 2:
    print("De palabra a número")

    opcion_2 = input("Cual es la palabra a convertir? ")

    if opcion_2 == "Uno":
        print("1")
    elif opcion_2 == "Dos":
        print("2")
    elif opcion_2 == "Tres":
        print("3")
    elif opcion_2 == "Cuatro":
        print("4")
    elif opcion_2 == "Cinco":
        print("5")
    elif opcion_2 == "Seis":
        print("6")
    elif opcion_2 == "Siete":
        print("7")
    else:
        print("No registrado")

else:
    print("No valido")

print("Fin")
