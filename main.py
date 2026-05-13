from models.equipo import Equipo
from services.torneo_service import registrar_torneo
from services.torneo_service import guardar_torneo
from services.reportes_service import guardar_equipo
from services.reportes_service import mostrar_equipos
from services.partido_service import registrar_equipo

while True:
    print("\n=== POLIMUNDIAL ===")
    print("1. Configuración del Torneo. ")
    print("2. Registrar Resultados. ")
    print("3. Ver Informes. ")
    print("4. Salir. ")
    # ------------------------------------------------------------------------------------------------------------------------------------ #
    opcion = input("Seleccione una opción: ")
    match opcion:

        case "1":
            print("\n=== CONFIGURACIÓN DEL TORNEO ===")
            torneo = registrar_torneo("torneo")
            guardar_torneo(torneo)
            print("\n=== REGISTRAR EQUIPO 1 ===")
            team1 = registrar_equipo("team1")
            guardar_equipo(team1)
            print("\n=== REGISTRAR EQUIPO 2 ===")
            team2 = registrar_equipo("team2")
            guardar_equipo(team2)
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
