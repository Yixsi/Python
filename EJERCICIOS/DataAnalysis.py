import matplotlib.pyplot as plt
#Gráfico usando listas
x1=[2,5,6,14]
y1= [11,22,33,44]

x2=[2,5,6,15]
y2=[4,12,18,45]
#Graficar 2 líneas en la misma grid
# plt.plot(x1,y1, color="blue", linewidth = 3, label = 'Línea 1')
# plt.plot(x2,y2, color="green", linewidth = 3, label = 'Línea 2')

# plt.title('Dos líneas juntas')
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.legend()
# plt.grid()
# plt.show()

#Gráfico de barras. Cuando coinciden la misma X, las apila
plt.bar(x1,y1, color="blue", linewidth = 3, label = 'Barra 1')
plt.bar(x2,y2, color="green", linewidth = 3, label = 'Barra 2')

plt.title('Dos Barras juntas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid()
plt.show()