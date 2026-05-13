from models.equipo import Equipo
from services.reportes_service import guardar_equipo
from services.reportes_service import mostrar_equipos
from services.partido_service import registrar_equipo
while True:
    print("\n=== POLIMUNDIAL ===")
    print("1. Registrar equipo")
    print("2. Registrar Resultados")
    print("3. Ver Informes")
    print("4. Salir")
    # ------------------------------------------------------------------------------------------------------------------------------------ #
    opcion = input("Seleccione una opción: ")
    match opcion:

        case "1":
            print("\n=== REGISTRAR EQUIPO ===")
            team = registrar_equipo("team")
            guardar_equipo(team)
            print("Torneo registrado correctamente.")

        case "2":
            print("\n=== REGISTRO DE RESULTADOS ===")
            print("estoy en el caso 2")

        case "3":
            print("\n=== INFORMES ===")
            print("estoy en el caso 33")
            mostrar_equipos()

        case "4":
            print("Saliendo del coso...")
            break

        case _:
            print("NO")