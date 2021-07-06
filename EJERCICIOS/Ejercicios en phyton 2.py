
# word = input("Ingresa una palabra: ").lower()
# newStr = ""
# for i in word:
#     if (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u'):
#         continue
#     else:
#         newStr += i
# print(newStr)

# palabra = input("Digite la palabra: ").lower()
# for i in 'aeiou':
#     palabra = palabra.replace(i, "")
# print(palabra)

# palabra = input("Ingresa una palabra: ").lower()
# for i in palabra:
#     if (i!='a') and (i!='e') and (i!='i') and (i!='o') and (i!='u'):
#         print(i, end="")

# comprobar = True
# while comprobar:
#     n = int(input("Ingrese un número entero: "))
#     if n > 0:
#         comprobar = False
#         for i in range(1, n+1, 2):
#             for j in range(i, 0, -2):
#                 print(j, end=" ")
#             print("")
#     else:
#         print("El número debe ser mayor a cero.")

    
# numbers = int(input("< "))
# for i in range(1, numbers + 1):
#     print(" ")
#     for j in range(i):
#         print(i, end=" ")

# password = "contraseña"
# while True:
#     dato = str(input("Ingrese la contraseña: "))
#     if dato == password:
#         print("La contraseña es correcta")
#         break
#     else:
#         print("Incorrecto. Inténtelo nuevamente.")
# lista = []
# while True:
#     n = int(input("Ingresa un número mayor a cero: "))
#     if n > 0:
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 lista.append(i)
#         if len(lista) == 2:
#             print(n, " es un número primo.")
#             break
#         else:
#             print(n, " no es un número primo.")
#     else:
#         print("Incorrecto")

# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")

# n = int(input("Introduce un número entero positivo mayor que 2: "))
# for i in range(2, n):
#     if n % i == 0:
#         break
# if (i + 1)  == n:
#     print(str(n) + " es primo")
# else: 
#     print(str(n) + " no es primo")

# word = input("Introduce una palabra: ")
# word = word[::-1]
# for i in word:
#     print(i)

# print("Ingresa una frase, seguida de una letra:")
# phrase = input().lower()
# letter = input().lower()
# count = 0
# for i in phrase:
#     if letter == i:
#         count += 1
# print(count)

# print("Escribe algo: ")
# phrase = input().lower()
# while phrase != "salir":
#     print(phrase)
#     phrase = input().lower()

# vocales = ('a','e','i','o','u')
# cadena = [''+i for i in vocales]
# print(cadena)

n_word = ['4' if l=='a' else '3' if l=='e' else l for l in input("Palabra: ").lower()]
print((''.join(n_word).capitalize()))
