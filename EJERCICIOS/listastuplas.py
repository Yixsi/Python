# subjects = ["matemáticas","física","química","historia","lenguaje"]
# for subject in subjects:
#     print("Yo estudio " + subject)

# subjects = ["matemáticas","física","química","historia","lenguaje"]
# for subject in subjects:
#     print("Yo estudio " + subject)

# subjects = [""]
# notas = [""]
# num = int(input("Ingrese el número de asignaturas: "))
# comprobar = True
# while comprobar:
#     if num > 0:
#         for i in range(num):
#             subject = input("Ingresa la asignatura: ")
#             subjects.append(subject)
#             nota = float(input("Ingresa la nota: "))
#             notas.append(nota)
#         comprobar = False
#     else:
#         num = int(input("Incorrecto. Ingrese el número de asignaturas: "))

# for i in range(1, num+1):
#     print("Su nota en la asignatura ", subjects[i], " es ", notas[i])

# lista = list(range(1, 11))
# lista.reverse()
# print(lista)

# alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O",
#  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# for letter in range(26, -1, -1):
#     if letter % 3 == 0:
#         alphabet.pop(letter)
# print(alphabet)

# word = input("Ingresa una palabra: ")
# word = list(word)
# rev_word = word
# rev_word = list(rev_word)
# rev_word.reverse()
# if word == rev_word:
#     print("Es un palíndromo")
# else:
#     print("No es un palíndromo")

# def numero_fijo(number: str):
#     index_1 = int(number.find('-'))
#     index_2 = int(number.find('-', index_1+1))
#     numero = number[index_1 + 1 : index_2]
#     return numero

# print(numero_fijo("+1-3235981692-24"))

