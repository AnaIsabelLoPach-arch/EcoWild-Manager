
# Listas para guardar la información
mascotas = []
propietarios = []
citas = []


# Registrar mascota
def registrar_mascota():
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")

    mascota = {
        "Nombre": nombre,
        "Especie": especie
    }

    mascotas.append(mascota)
    print("Mascota registrada correctamente.\n")


# Registrar propietario
def registrar_propietario():
    nombre = input("Nombre del propietario: ")
    telefono = input("Teléfono: ")

    propietario = {
        "Nombre": nombre,
        "Teléfono": telefono
    }

    propietarios.append(propietario)
    print("Propietario registrado correctamente.\n")


# Registrar cita
def registrar_cita():
    mascota = input("Nombre de la mascota: ")
    fecha = input("Fecha de la cita: ")

    cita = {
        "Mascota": mascota,
        "Fecha": fecha
    }

    citas.append(cita)
    print("Cita registrada correctamente.n")


# Mostrar mascotas
def ver_mascotas():

    print("n ===== MASCOTAS =====")

    if len(mascotas) == 0:
        print("No hay mascotas registradas.")

    else:
        for mascota in mascotas:
            print("-------------------")
            print("Nombre :", mascota["Nombre"])
            print("Especie:", mascota["Especie"])

    print()


# Mostrar propietarios
def ver_propietarios():

    print("n ===== PROPIETARIOS =====")

    if len(propietarios) == 0:
        print("No hay propietarios registrados.")

    else:
        for propietario in propietarios:
            print("-------------------")
            print("Nombre   :", propietario["Nombre"])
            print("Teléfono :", propietario["Teléfono"])

    print()


# Mostrar citas
def ver_citas():

    print("n ===== CITAS =====")

    if len(citas) == 0:
        print("No hay citas registradas.")

    else:
        for cita in citas:
            print("-------------------")
            print("Mascota :", cita["Mascota"])
            print("Fecha   :", cita["Fecha"])

    print()


# Menú principal
opcion = ""

while opcion != "7":

    print("=================================")
    print("        EcoWild Manager")
    print("=================================")
    print("1. Registrar mascota")
    print("2. Registrar propietario")
    print("3. Registrar cita")
    print("4. Ver mascotas")
    print("5. Ver propietarios")
    print("6. Ver citas")
    print("7. Salir")

    opcion = input("n Seleccione una opción: ")

    if opcion == "1":
        registrar_mascota()

    elif opcion == "2":
        registrar_propietario()

    elif opcion == "3":
        registrar_cita()

    elif opcion == "4":
        ver_mascotas()

    elif opcion == "5":
        ver_propietarios()

    elif opcion == "6":
        ver_citas()

    elif opcion == "7":
        print("n Gracias por utilizar EcoWild Manager.")

    else:
        print("n Opción no válida")