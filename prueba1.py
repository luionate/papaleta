#FUNCONES
def buscar_mascota (lista_m, nombre_m):
    for x in range(lista_m):
        #verificacion si el nombre coincide
        if nombre_m == lista_m[x]["nombre"]:
            return x #renorto la posición
        #si no lo encuentro
        return -1
#validaciones
def validar_nombre(name):
    #una funcion que elimina los espacions el inicaio y al final de un string y si queda vacia devuelve un false
    return name.strip() != "" #Retorna True si es valido- False si es invalido

def validar_especie(especie):
    #Verificr que es un perro, gato o ave solamente(Sin diferenciar mayusculas o minusculas)
    especies_validad = ["perro","gato","ave"]
    return especie.strip().lower() in especies_validad
def validar_edad(edad):
    #que sean numeros y mayor a 0
    #isdigit() -> revisa que el strig contenga solo digitos(no negativo, no decimal)
    return edad.isdigit() and int(edad) > 0
     
def mostrar_menu():
    print("======MENÚ PRINCIPAL========")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar mascota")
    print("6.- Salir")
    print("============================")
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Selecione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Debe selecionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return opcion
#Funcion para agregar mascota
#opcion1
def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    #llamar la funcion que valida nombre para mostrar el mesaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacío")
        return
    especie = input("Ingrese la especie de la mascota (Perro, Gato o Ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie debe ser Perro, Gato o Ave")
        return
    edad = input("Ingrese la edad de la mascota")
    correcto = validar_edad(edad)
    if not correcto:
        print("La edad debe ser un numero entero y mayor a cero")
        return
    #aqui agrego el diccionario
    mascota ={
        "nombre": nombre.strip(),
        "especie": especie.strip(),
        "edad": int(edad),
        "vacunada": False
    }
    lista.append(mascota)
    print("Mascota agregada correctamente")
#opcion 4
def actualizar_vacunas(lista_m):
    #recorrer lista
    for m in lista_m:
        #validar la edad
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
#CODIGO PRINCIPAL
#declaro la lista de mascota

lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()
    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        print("*****Buscar mascota******")
        nombre = input("Ingrese el nombre de  la  mascota: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #almacenar el diccionariop en una variable
        if posicion != -1:
            print(f"La posicion encontrada es: {m["nombre"]}")
            m = lista_mascotas[posicion]
            print(f"especie mascota: {m["especie"]}")
            print(f"Edad mascota: {m["edad"]}")
            print(f"Vacunada: {m["vacunada"]}")
        else: 
            print("La mascota no se ha encontrado")
            
    elif op == 3:
        print("*****Eliminar Mascota****")
        nombre = input("Ingrese nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        if posicion != -1:
            lista_mascotas.pop(posicion)
            print("La mascota ha sido eliminada de la lista")
        else:
            print(f"La mascota {nombre} no se encuentra en la lista")

    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("Vacunas actualizadas")
    elif op == 5:
        #actualizar las vacunas
        actualizar_vacunas(lista_mascotas)
        #mostrar los datos de las mascotas
        if len(lista_mascotas) == 0:
            print("No hay masotas en la lista")
        else:
            print("==Lista de mascotas ==")
            for m in lista_mascotas:
                print(f"Nombre: {m["nombre"]}")
                print(f"especie: {m["especie"]}")
                print(f"Edad: {m["edad"]}")
                estado = "AL DIA" if m["vacunada"] else "PENDIENTE"
                print(f"Vacunada: {m["estado"]}")
                print("==========================")
                
    elif op == 6:
        print("Gracias por usar el sistema")
