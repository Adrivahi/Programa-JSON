import ListaFunciones

def mostrar_menu():
    print("Menú:")
    print("1. Listar equipos")
    print("2. Contar jugadores de un equipo")
    print("3. Filtrar jugadores por posición y equipo")
    print("4. Mostrar información de un jugador")
    print("5. Quiz")
    print("0. Salir")

mostrar_menu()
Funcionando = True

while Funcionando:
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ListaFunciones.listar_equipos()
    elif opcion == '2':
        ListaFunciones.contar_jugadores_por_equipo()
    elif opcion == '3':
        ListaFunciones.listar_jugadores_por_posicion()
    elif opcion == '4':
        ListaFunciones.obtener_info_jugador()
    elif opcion == '5':
        ListaFunciones.ejercicio_quiz()
    elif opcion == "0":
        print("¡Hasta luego!")
        Funcionando = False
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")