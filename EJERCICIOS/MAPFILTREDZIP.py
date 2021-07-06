'''Problema #1:
Utilizar la función incorporada map() para crear una función que retorne una lista con la
longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena
de texto y retornará una lista.'''

def len_words()->list:
    phrase = input("Enter a phrase: ")
    len_words = list(map(len, phrase.split()))
    return len_words
# print(len_words())

'''Problema #2:
Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función
reduce.'''

from functools import reduce
def number(lista):
    full_number = reduce(lambda acum, elem: acum*10+elem, lista) #el acumulador inicia en cero
    return full_number

#print(number([3,5,6,7]))

'''Problema #3:
Crear una función que retorne las palabras de una lista de palabras que comience con una
letra en específico. Utilizar la función filter.'''

def words():
    n = int(input("Ingrese el número de palabras deseado: "))
    letter = input("Ingrese la letra de comparación: ").lower()
    lista = []
    i=1
    while i<=n:
        n_word = input("Palabra: ").lower()
        lista.append(n_word)
        i+=1
    return list(filter(lambda n_word: n_word[0]==letter, lista))
#print(words())

def words():
    n = int(input("Ingrese el número de palabras deseado: "))
    letter = input("Ingrese la letra de comparación: ").lower()
    lista = [input("Palabra: ").lower() for i in range(1,n+1)]
    return list(filter(lambda n_word: n_word[0]==letter, lista))
#print(words())

'''Problema #4:
Realizar una función que tome una lista de comprensión para devolver una lista de la misma
longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre
ellas. Ejemplo: Listas: ['A', 'a'] ['B','b'] Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función
zip.'''

#Solución:
def concatenacion(L1, L2, connector):
 return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
#print(concatenacion(['A', 'a'],['B','b'],'-')) #salida no esperada

'''Problema #5:
Realizar una función que tome una lista y retorne un diccionario que contenga los valores de
la lista como clave y el índice como el valor. Utilizar la función enumerate.'''
def enumerate_use()->dict:
    lista = list(range(1, 11))
    dictionary = {key: value for value, key in enumerate(lista)}
    return dictionary
#print(enumerate_use())

'''Problema #6:
Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo
valor es igual a su índice. Utilizar la función enumerate.'''

def lista_len(lista):
    acum = 0
    for idx, value in enumerate(lista):
        if idx == value:
            acum +=1
    return acum
#print(lista_len([4, 5, 2, 2, 4, 5]))

def count_match_index(L):
    return len([num for count,num in enumerate(L) if num==count]) #crea lista, verifica la cantidad con len
#print(count_match_index([0,2,2,1,5,5,6,10]))

'''Recursión con lambda'''
fact = lambda x: x*fact(x-1) if x>1 else 1
# print(fact(5))
