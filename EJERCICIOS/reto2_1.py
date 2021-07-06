def reto_2(client: int, name: str, address: str, phone: int, member: bool, bd_clientes: dict) -> dict:
    
    datos = name.split(' ')
    name = datos[0].upper()
    surname = datos[1].upper()

    dicc = {'nombre': name,
            'apellido': surname,
            'direccion': address,
            'telefono': phone,
            'membresia': member}
    if isinstance(client, int) == True:
        if client not in bd_clientes:
            bd_clientes[client] = dicc
            return_message = f"El cliente {client} se agregó a la base de datos."
        elif dicc != bd_clientes[client]:
            bd_clientes[client] = dicc
            return_message = f"Cliente {client}, actualizado en la base de datos"
        else:
            return_message = f"El cliente {client} Se encuentra en la base de datos"
    else:
        return_message = f"Ingrese un id de tipo valido."

    return return_message

def bd_clientes():
    clientes = {

        34043243: {
            'nombre': 'HOMERO',
            'apellido': 'SIMPSON',
            'direccion': 'avenida siempreviva 742',
            'telefono': 46637600,
            'membresia': False
        },
        42140704: {
            'nombre': 'MARGE',
            'apellido': 'SIMPSON',
            'direccion': 'siempreviva',
            'telefono': 46637600,
            'membresia': True
        },
        21015602: {
            'nombre': 'NED',
            'apellido': 'FLANDERS',
            'direccion': 'avenida siempreviva 864',
            'telefono': 63392730,
            'membresia': True
        },
        26677308: {
            'nombre': 'MOU',
            'apellido': 'SZYSLAK',
            'direccion': 'calle wualnut 668',
            'telefono': 76484377,
            'membresia': False
        },
        16361910: {
            'nombre': 'MONTY',
            'apellido': 'BURNS',
            'direccion': 'mansion burns',
            'telefono': 24275370,
            'membresia': True
        },
    }

    return clientes

clientes = bd_clientes()
print(reto_2(34043243, 'Homero Simpson', 'AVENIDA SIEMPREVIVA 742', 46637600, False, clientes))
print(clientes.get(34043243, 'Ciente no se encuentra en BD.'))

clientes = bd_clientes()
print(reto_2(42140704, 'marge simpson', 'avenida siempreviva 742', 46637600, True, clientes))
print(clientes.get(42140704, 'Ciente no se encuentra en BD.'))

clientes = bd_clientes()
print(reto_2('cc24687900', 'pepito perez', 'CL Perezlandia ESQ.', 3036052, True, clientes))
print(clientes.get('24687900', 'Ciente no se encuentra en BD.'))

clientes = bd_clientes()
print(reto_2(24687900, 'pepito perez', 'CL Perezlandia ESQ.', 3036052, True, clientes))
print(clientes.get(24687900, 'Ciente no se encuentra en BD.'))