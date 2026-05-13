import json
def guardar_equipo(equipo):
    try:
        with open("data/equipos.json", "r") as archivo:
            equipos = json.load(archivo)
    except:
        equipos = []
    nuevo_equipo = {
        "pais": equipo.pais,
        "abrev": equipo.abrev,
        "grupo": equipo.grupo,
        "confederacion": equipo.confederacion
    }
    equipos.append(nuevo_equipo)
    with open("data/equipos.json", "w") as archivo:
        json.dump(equipos, archivo, indent=4)

def mostrar_equipos():
    with open("data/equipos.json", "r") as archivo:
        equipos = json.load(archivo)
    for equipo in equipos:
        print(f"""País: {equipo['pais']}
Grupo: {equipo['grupo']}
Confederación: {equipo['confederacion']}""")