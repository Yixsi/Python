# lista = []
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")



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

# i = 1
# while i<=5:
#     print("*"*i)
#     i += 1

# n = int(input("Ingresa un rango de números: "))
# for x in range(1, n+1):
#     if ((x % 3 == 0) and (x % 5 == 0)):
#         print("SoloLearn")
#     elif x % 2 == 0:
#         continue       
#     elif x % 3 == 0:
#         print("Solo")
#     elif x % 5 == 0:
#         print("Learn")
#     else:
#         print(x)

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz", end=' ')
#         elif i % 5 == 0:
#             print("buzz", end= ' ')
#         elif i % 3 == 0:
#             print("fizz", end=' ')
#         else:
#             print(i, end=' ')
    
#     print()


# fizzbuzz()

# fila = 1
# while fila <= 5:
#     i = 1
#     while i <= fila:
#         print('*', end='')
#         i += 1
#     print()
#     fila +=1

# i = 1
# while i<=5:
#     print("*"*i)
#     i += 1

number = int(input("Ingrese un número: "))
def show_number(number):
    if number<0:
        return
    elif number !=0:
        print(number)
        return show_number(number-1)

show_number(number)
