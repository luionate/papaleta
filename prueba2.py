#Funciones+
#Mostrar Menú
def mostrar_menu():
    print("======MENÚ PRINCIPAL========")
    print("1.- Agregrar Reserva")
    print("2.- Buscar Reserva")
    print("3.- Eliminar Rserva")
    print("4.- Confirmar Reserva")
    print("5.- Mostrar Reserva")
    print("6.- Salir")
    print("============================")
#Retornar laopcion del meu elegida por el usuario
def ingresar_opcion():
    while True:
        try:    
            op = int(input("Seleccione una opcion: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ingresar un numero del 1 al 6")
#opcion 1
#Funcion para agreagar
def agregar_reserva(lista_r):
    nombre_completo = input("Ingrese su nombre completo: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacio")
        return
    
    numero_habitacion = input("Ingrese el numero de habitacion a reservar: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("L a habitacion debe ser un numero entero entre 1 y 200")
        return
    
    cant_noches = input("Ingrese la cantadad de noches a hospedarse: ")
    correcto = validar_noches(cant_noches)
    if not correcto:
        print("La cantidad de noches debe ser mayor a 0")
        return
    #agregamos diccionario
    reserva = { 
        "husped" : nombre_completo.strip().upper(),
        "habitacion" : int(numero_habitacion),
        "noches" : int(cant_noches),
        "confirmada" : False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente")
#opcion 2
def buscar_reserva(lista_r, huesped):
    #recorrer la lista 
    for x in range(len(lista_r)):
        #verificar si existe dentro
        if huesped == lista_r[x]["husped"]:
            return x
    return -1
#opcion4
def confirmar_reserva(lista_r):
    for i in lista_r:
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False
#opcion5
def mostrar_reserva(lista_r):
    print("========Listad de Reservas ======")
    for i in lista_r:
        print(f"Huesped: {i["huesped"]}")
        print(f"Habitacion: {i["habitacion"]}")
        print(f"Noches: {i["noches"]}")
        if i["confirmada"]:
            print("Estado: Confirmado")
        else:
            print("Estado: Pendiente")
        print("============================")
#Funcionesd de validacion
def validar_huesped(nombre):
    return nombre.strip() != ""
def validar_habitacion(hab):
    if hab.isdigit():
        validar = int(hab)
        return validar >= 1 and validar <= 200
    return False
def validar_noches(noches):
    if noches.isdigit():
        validar = int(noches)
        return validar > 0
    return False


    #Codigo Principal
