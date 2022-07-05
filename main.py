import gestor as gp

while True:
    opcion=input("""\nIngrese una opcion
    1. Agregar equipo
    2. Agregar resultado
    3. Mostrar posiciones
    4. Salir

    Opcion: """)
    if opcion == "1":
        gp.nuevo_equipo()
    elif opcion == "2":
        gp.agregar_resultado()
    elif opcion == "3":  
        gp.mostrar_posicion()
    elif opcion == "4":
        break
    else:
        print("\nValor ingresado incorrecto, reintentar.")