# Escribir un programa que guarde en una variable 
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo 
# o un mensaje de aviso si la divisa no está en el diccionario.
# 
# def divisas():
#     divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#     ndivisa = input("¿Qué símbolo de divisa deseas consultar?: ").title() 
#     #Método title() vuelve la primera letra mayúscula
#     if ndivisa in divisas:
#         print(f"El símbolo de la divisa {ndivisa} es {divisas[ndivisa]}.")
#     else:
#         print("La divisa no se encuentra en el diccionario.")
# divisas()

#Escribir un programa que pregunte al usuario su nombre, 
#edad, dirección y teléfono y lo guarde en un diccionario.
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
# vive en <dirección> y su número de teléfono es <teléfono>.

# data = {}
# def getUser_data():
#     global data
#     data = {
#         'name': input("Ingrese su nombre: "),
#         'age': int(input("Ingrese su edad: ")),
#         'direction': input("Ingrese su dirección: "),
#         'phone': input("Ingrese su No. telefónico: ")
#     }
# def showUser_data():
#     getUser_data()
#     print(f"{data['name']} tiene {data['age']} años, vive en {data['direction']} y su número de teléfono es {data['phone']}")

# showUser_data()

# Escribir un programa que guarde en un diccionario los precios de las frutas 
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
# pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario
# debe mostrar un mensaje informando de ello.
#Tabla
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# costo_frutas = dict(plantain = 1.35, apple = 0.80, pear = 0.85, orange = 0.70)
# def costo_total():
#     fruit = input("Which fruit would you like?: ").lower()
#     if fruit in costo_frutas:
#         weight= float(input("Enter the weight in kilograms: "))
#         total = round(weight*costo_frutas[fruit], 2)
#         print(f"Your total is {total}")
#     else:
#         print(f"Sorry, there's no {fruit} at the moment.")
# costo_total()

# Escribir un programa que pregunte una fecha en formato
# dd/mm/aaaa y muestre por pantalla la misma fecha en formato
# dd de <mes> de aaaa donde <mes> es el nombre del mes.

# months = {1:'enero', 2:'febrero',3:'marzo', 4:'abril', 5:'mayo',
# 6:'junio', 7: 'julio',8:'agosto', 9:'septiembre', 10:'octubre',
# 11:'noviembre', 12:'diciembre'}
# def getDate():
#     date = input("Ingrese la fecha en formato dd/mm/aaaa: ")
#     date = date.split('/')
#     print(date[0], 'de', months[int(date[1])], 'de', date[2])
# getDate()

# Cree un diccionario en el que las llaves sean una tupla entre los números del 3 al 10 y su respectivo cubo.
# Y dónde los valores sean las listas con los cuadrados de los números de dos en dos, entre el 4 y el 30,
# que son divisibles enteros con el primer elemento de su llave correspondiente.

# dictionary = dict()
# for i in range(3, 11):
#     dictionary[(i, i**3)] = []
#     for j in range(4, 31, 2):
#         if j % i == 0:
#             dictionary[(i, i**3)].append(j**2)    
# print(dictionary)

#Cree nuevamente la lista y el diccionario anterior, en una sola línea.

# dictionary =  {(i, i**3) : [ j**2 for j in range(4,31,2) if j%i == 0 ] for i in range(3, 11) }
# print(dictionary)

# Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario
# con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
# para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# translator = {}
# comprobar = True
# print("Ingrese cada pareja de palabra y su traducción en formato 'word: translation,' separados por comas. ")
# def getTranslation():
#     global translator
#     translator ={
#         input(): input(),
#     }
# while comprobar:
#     key = input()
#     value = input()
#     translator.append(getTranslation())
    
# diccionario = {}
# palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
# for i in palabras.split(','):
#     clave, valor = i.split(':cl')
#     diccionario[clave] = valor
# frase = input('Introduce una frase en español: ')
# for i in frase.split():
#     if i in diccionario:
#         print(diccionario[i], end=' ')
#     else:
#         print(i, end=' ')


divisores = {}

divisores = {i:{j: j*j for j in range(1, i+1) if i%j==0} for i in range(1, 11)}
print(divisores)

divisores = {}

for i in range(1, 11):
    divisores[i] = {} 
    for j in range(1, i +1):
        if i % j == 0: 
            divisores[i].update({j:j**2})
print(divisores)