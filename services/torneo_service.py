import json
from models.torneo import Torneo
def guardar_torneo(torneo):
    try:
        with open("data/torneos.json", "r") as archivo:
            torneos = json.load(archivo)
    except:
        torneos = []
    nuevo_torneo = {
        "nombre": torneo.nombre,
        "inicio": torneo.inicio,
        "fin": torneo.fin,
        "cerrar_confi": torneo.cerrar_confi
    }
    torneos.append(nuevo_torneo)
    with open("data/torneos.json", "w") as archivo:
        json.dump(torneos, archivo, indent=4)

def mostrar_torneos():

    with open("data/torneos.json", "r") as archivo:
        torneos = json.load(archivo)
    for torneo in torneos:
        print(f"""Nombre: {torneo['nombre']}
Inicio: {torneo['inicio']}
Fin: {torneo['fin']}
Estado cerrado: {torneo['cerrar_confi']}
""")
        
def registrar_torneo(torneo):
    nombre = input("Ingrese el nombre del torneo: ")
    inicio = input("Ingrese el inicio del torneo: ")
    fin = input("Ingrese el fin del torneo: ")
    torneo = Torneo(nombre, inicio, fin)

    return torneo
