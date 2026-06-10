#Funciones
def ficha_producto(nombre, precio, stock):#noo importa el orden de los parametros
    print("=====================")
    print(f"Nombre del producto: {nombre} ||")
    print(f"Stock del producto: {stock} ||")
    print(f"Precio del producto: {precio} ||")
    print("=====================")
    

#Codigo principal
nombre1 = input("Ingrese el nombre del producto: ")
while True:
    try:
        stock1 = int(input("Ingrese el stock del producto: "))
        if stock1 < 0:
             print("Debe ser mayor o igual a 0")
        else:
             break        
    except ValueError:
        print("Debe ingresar numeros")

while True:   
    try:
        precio1 = int(input("Ingrese el precio del producto: "))
        if precio1 <= 0:
            print("Debe ser un valor positivo")
        else:
            break  
    except ValueError:
            print("Debe ingresar numeros")

ficha_producto(nombre1, precio1, stock1)#Debemos enviarlo en el mismo orden que los creamos en la funcion