#FUNCONES
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
#CODIGO PRINCIPAL
#declaro la lista de mascota
lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()





if op = 1:
elif op = 2:
elif op = 3:
elif op = 4:
elif op = 5:
elif op = 6:


    