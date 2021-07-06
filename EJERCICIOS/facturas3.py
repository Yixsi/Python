facturas = {'A1':1000,'A2':3520, 'A3':45000}

def AgregarFactura():

    NFactura=input('Numero de factura a agregar: ').upper()
    if NFactura in facturas:
        print(f'FActura {NFactura} ya esta ingresada verifique el numero...')
    else:
     VFactura=int(input('Valor de la factura: '))
     facturas.update({NFactura:VFactura})
    print() 
    return facturas
 
def PagarFactura():

     NFactura = (input("Ingrese el numero de la Factura a pagar: ")).upper()
     if NFactura in facturas: 
         print(f'La factura {NFactura} esta paga')
         Facturado =0
         Facturado+=facturas.pop(NFactura)
         print(Facturado)
         X=sum(facturas.values())
         print(F'CANTIDAD COBRADA {Facturado} $, CANTIDAD POR COBRAR: {X} $')
         print()  
     return facturas

def menu():

    TITLE="--APLICACION CRUD: GESTION DE FACTURAS--"
    X=TITLE.center(100)
    print(X)
    Y='='*50
    print(Y.center(100))
    print("ESCOJA UNA OPCION ".center(100))
    print("[C] - AGREGAR FACTURA".center(100))
    print("[R] - PAGAR FACTURA".center(98))
    print("[E] - SALIR.".center(90))
    print(Y.center(100))
    print()
    command=input
       
if __name__=='__main__':

    mainloop = True
    while mainloop: 

        menu()
        command = input()
        command = command.upper()        

        if command == 'C':
           print("-> Adicionando Factura".center(100)) 
           AgregarFactura()
           print()
           print('Facturas registradas',facturas)     
           X=sum(facturas.values())
           print(F'CANTIDAD COBRADA {X-X} $, CANTIDAD POR COBRAR: {X} $')
           print()               

        elif command == 'R':
         PagarFactura()
         print('Facturas registradas',facturas)     
         print()             

        elif command == 'E':
          print("Ha salido exitosamente.")
          mainloop = False

        else:
            print("OPCION INVALIDA")
