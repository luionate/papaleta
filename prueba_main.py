import prueba2 as p
#codigo principal
opcion = 0
lista_reservas = []
while opcion != 6:
    p.mostrar_menu()
    opcion = p.ingresar_opcion()

    if opcion == 1:
        #llamar a la funcion que ingresa nuevas reservas
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        #solicitamos el nombre a buscar
        nombre = input("Ingrese el nombre del uesped a buscar: ")
        #llamamos a la funion encargada de buscar
        pos = p.buscar_reserva(lista_reservas, nombre)
        #validamos que retorna la funcion buscar
        if pos != -1:
            #se emcontro eñ huesped asi que muestro sus datos
            print("**********Reserva encontrada**********")
            print(f"Nombre del huesped: {lista_reservas[pos]["huesped"]}")
            print(f"Numero del habitacion: {lista_reservas[pos]["habitacion"]}")
            print(f"Noches del hospedaje: {lista_reservas[pos]["noches"]}")
            estado = "Confirmado" if lista_reservas[pos]["confirmada"] else "pediente"
            print(f"Estado: {estado}")
            print("***************************************")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")
            
    elif opcion == 3:
        nombre = input("Ingrese el nombre del uesped a buscar: ")
        #llamamos a la funion encargada de buscar
        pos = p.buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
        else:
            print(f"El huesped {nombre} no ha sido encontrado")

    elif opcion == 4:
        #llamamos a la funcion que confirma las reservas
        p.confirmar_reserva(lista_reservas)
    elif opcion == 5:
        p.confirmar_reserva(lista_reservas)
        p.mostrar_reserva(lista_reservas)
    elif opcion == 6:
        print("Gracias por usar el programa.Vuelva pronto")