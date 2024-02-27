import json

with open(r'C:\Users\AdriVaHi\Desktop\Clase\MARCA\JSON\players.json', encoding='utf-8') as archivo:
    Datos = json.load(archivo)

def listar_equipos():
    equipos = set()
    for player in Datos['players']:
        equipos.add(player['tid'])
    print("Equipos disponibles:")
    for equipo in equipos:
        print("-", equipo)

def contar_jugadores_por_equipo():
    equipos = {}
    for player in Datos['players']:
        equipo = player['tid']
        if equipo in equipos:
            equipos[equipo] += 1
        else:
            equipos[equipo] = 1
    print("Número de jugadores por equipo:")
    for equipo, num_jugadores in equipos.items():
        print(f"- {equipo}: {num_jugadores}")

def listar_jugadores_por_posicion():
    equipo = input("Introduce el nombre del equipo: ")
    posicion = input("Introduce la posición: ")
    print(f"Jugadores del equipo {equipo} que pueden jugar en la posición {posicion}:")
    for player in Datos['players']:
        if player['tid'] == equipo and player['pos'] == posicion:
            print("-", player['name'])

def obtener_info_jugador():
    nombre = input("Introduce el nombre del jugador: ")
    for player in Datos['players']:
        if player['name'] == nombre:
            print(f"Información de {nombre}:")
            print("- Año de nacimiento:", player['born']['year'])
            print("- Lugar de nacimiento:", player['born']['loc'])
            print("- Posición:", player['pos'])
            print("- Estadísticas de juego:", f"Altura (Pulgadas): {player['hgt']}, Peso (Libras): {player['weight']}")
            print("- Año en el que empezó a jugar:", player['draft']['year'])
            return
    print("El jugador no se encuentra en la base de datos.")

def ejercicio_quiz():
    import random
    filtered_players = [player for player in Datos['players'] if player['tid'] != "(Retirados)"]
    if filtered_players:
        player = random.choice(filtered_players)
        nombre = player['name']
        equipo = player['tid']
        respuesta = input(f"¿A qué equipo pertenece el jugador {nombre}? ")
        if respuesta == equipo:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. El jugador {nombre} pertenece al equipo {equipo}.")
    else:
        print("No hay jugadores disponibles para el quiz.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Listar equipos")
        print("2. Contar jugadores de un equipo")
        print("3. Filtrar jugadores por posición y equipo")
        print("4. Mostrar información de un jugador")
        print("5. Quiz")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_equipos()
        elif opcion == '2':
            contar_jugadores_por_equipo()
        elif opcion == '3':
            listar_jugadores_por_posicion()
        elif opcion == '4':
            obtener_info_jugador()
        elif opcion == '5':
            ejercicio_quiz()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
