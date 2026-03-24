salir = 0
correctaCategoria = 0
categorias = ("Comestibles", "Aseo", "Aseo Personal", "Golosinas")
productos = {"Libra Azucar": ["001", "Libra Azucar", 4000, 20, categorias[0]],  "Litro Leche": ["002", "Litro Leche", 4000, 10, categorias[0]],
             "Jabon Fab 500gr": ["003", "Jabon Fab 500gr", 5500, 25, categorias[1]]}
numeroSeleccionMenu = 0


def ingresarNumero (valor):
    try:
       numeroSeleccionMenu = int(valor)
       return numeroSeleccionMenu
    except ValueError:
        print("\n !!!! Debe digitar un valor numerico ¡¡¡¡")
        return ingresarNumero(input("Digite nuevamente el numero: "))
    
def imprimirCategorias ():
    contador = 0
    for categ in categorias:
        contador+=1
        print(f"{contador}. {categ}")
    





while salir == 0:
    print("\n #######--- Bienvenido al sistema de inventario de productos ---####### \n")
    
    seleccionMenu = ingresarNumero(input("Por favor, digite el numero de alguna de las siguientes opciones:\n  " \
        "1. Agregar un producto. \n  " \
        "2. Mostrar todos los productos. \n  " \
        "3. Buscar un producto. \n  " \
        "4. Eliminar un producto. \n  " \
        "5. Salir del programa. \n"))
        
    if seleccionMenu == 1:
        elementosNuevoProducto = []
        print("Agregar un producto")
        nombreProducto = input("Digite el nombre del producto: ")
        elementosNuevoProducto.append(input("Digite el codigo del producto: "))
        elementosNuevoProducto.append(nombreProducto)
        elementosNuevoProducto.append(ingresarNumero(input("Digite el precio del nuevo producto: "))) 
        elementosNuevoProducto.append(ingresarNumero(input("Digite el inventario del nuevo producto: "))) 
        while correctaCategoria == 0: 
            imprimirCategorias()
            seleccionCategoria = ingresarNumero(input(f"Digite el numero de la categoria del prodcuto: \n"))
            seleccionCategoria -= 1
            if seleccionCategoria < len(categorias) and seleccionCategoria >= 0:
                elementosNuevoProducto.append(categorias[seleccionCategoria])
                correctaCategoria = 1
            else:
                print("Ha dijitado un numero que no esta asociado a ninguna categoria \n Digite nuevamente el numero de la categoria del producto")
        productos[nombreProducto] = elementosNuevoProducto
        print("PRODUCTO AGREGADO CORRECTAMENTE")
    elif seleccionMenu == 2:
        print("Mostrar todos los productos.")
        for nombreProd in productos.keys():
            print(nombreProd)
    elif seleccionMenu == 3:
        print("Buscar un producto.")
        prodaBuscar = input("Digite el nombre del producto a buscar: ")
        if prodaBuscar in productos:
            print(f"{prodaBuscar}:  {productos[prodaBuscar]}")
        else:
            print(f"No se ha encontrado el producto {prodaBuscar}")
    elif seleccionMenu == 4:
        print("Eliminar un producto")
        prodaBuscar = input("Digite el nombre del producto a eliminar: ")
        if prodaBuscar in productos:
           valorEliminado = productos.pop(prodaBuscar)
           print(f"Se ha eliminado el producto {valorEliminado}")
        else:
            print(f"No se ha encontrado el producto {prodaBuscar}")
    elif seleccionMenu == 5:
        print("Salir del programa")
        salir = 1
    else:
        print("\n !!!! Debe digitar un numero valido ¡¡¡¡")

