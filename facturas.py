'''Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, 
pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su 
coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y 
se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla 
la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'''

facturas = {'01': 20000,'02': 35000, '03':12000}


def crear_factura(facturas, ide, costo):
    if ide not in facturas:    
        facturas[ide] = costo
    else:
        print(f'La factura {ide} se encuentra en lista')
    return facturas

pagado = 0
def delete_factura(ide):
    global pagado
    if ide in facturas:
        pagado += facturas.pop(ide)
        print("Se han pagado: ", pagado)
    else:
        print(f'La factura {ide} NO se encuentra en lista')
pendiente = 0
def pendiente_cobro():
    global pendiente
    
    for factura in facturas:
        pendiente += facturas[factura]
    print("Se tiene pendiente por pagar un total de: ", pendiente)
    pendiente = 0

def get_factura_ide():

    ide = None

    while not ide:
        ide = input('Ingrese no. de la factura: ')

    return ide

def print_menu():

    print("--APLICACIÓN CRUD: GESTIÓN DE FACTURAS--")
    print("="*50)
    print("Escoja su opción: ")
    print("[C] - Agregar factura")
    print("[P] - Pagar factura")
    print("[E] - Salir.")


if __name__ == '__main__':
    mainlopp = True

    while mainlopp:
        print_menu()

        command = input()
        command = command.upper()

        if command == 'C':
            ide = input("Ingrese el número de la factura: ")
            costo = int(input("Ingrese el costo de la factura: "))
            crear_factura(facturas, ide, costo)
            print(facturas)
        elif command == 'P':
            ide = get_factura_ide()
            delete_factura(ide)
            pendiente_cobro()
        elif command == 'E':
            mainlopp = False
        else:
            print("OPCION INVÁLIDA")
