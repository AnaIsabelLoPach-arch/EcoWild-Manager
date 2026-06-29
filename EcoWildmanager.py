# EcoWild Manager

mascotas = []
propietarios = []
citas = []

opcion = ""

while opcion != "7":

    print("\n====== EcoWild Manager ======")
    print("1. Registrar mascota")
    print("2. Registrar propietario")
    print("3. Registrar cita")
    print("4. Ver mascotas")
    print("5. Ver propietarios")
    print("6. Ver citas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre de la mascota: ")
        especie = input("Especie: ")

        mascotas.append({
            "Nombre": nombre,
            "Especie": especie
        })

        print("Mascota registrada.")

    elif opcion == "2":

        nombre = input("Nombre del propietario: ")

        propietarios.append({
            "Nombre": nombre
        })

        print("Propietario registrado.")

    elif opcion == "3":

        mascota = input("Nombre de la mascota: ")
        fecha = input("Fecha de la cita: ")

        citas.append({
            "Mascota": mascota,
            "Fecha": fecha
        })

        print("Cita registrada.")

    elif opcion == "4":

        print("\nMascotas:")

        for mascota in mascotas:
            print(mascota)

    elif opcion == "5":

        print("\nPropietarios:")

        for propietario in propietarios:
            print(propietario)

    elif opcion == "6":

        print("\nCitas:")

        for cita in citas:
            print(cita)

    elif opcion == "7":

        print("Gracias por usar EcoWild Manager.")

    else:

        print("Opción no válida.")
mascotas = []
propietarios = []
citas = []

opcion = ""

while opcion != "7":

    print("\n====== EcoWild Manager ======")
    print("1. Registrar mascota")
    print("2. Registrar propietario")
    print("3. Registrar cita")
    print("4. Ver mascotas")
    print("5. Ver propietarios")
    print("6. Ver citas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre de la mascota: ")
        especie = input("Especie: ")

        mascotas.append({
            "Nombre": nombre,
            "Especie": especie
        })

        print("Mascota registrada.")

    elif opcion == "2":

        nombre = input("Nombre del propietario: ")

        propietarios.append({
            "Nombre": nombre
        })

        print("Propietario registrado.")

    elif opcion == "3":

        mascota = input("Nombre de la mascota: ")
        fecha = input("Fecha de la cita: ")

        citas.append({
            "Mascota": mascota,
            "Fecha": fecha
        })

        print("Cita registrada.")

    elif opcion == "4":

        print("\nMascotas:")

        for mascota in mascotas:
            print(mascota)

    elif opcion == "5":

        print("\nPropietarios:")

        for propietario in propietarios:
            print(propietario)

    elif opcion == "6":

        print("\nCitas:")

        for cita in citas:
            print(cita)

    elif opcion == "7":

        print("Gracias por usar EcoWild Manager.")

    else:

        print("Opción no válida.")