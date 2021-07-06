def reto_4(dictionary: dict)->tuple:
    a = [[5 if value[j] < 6 else value[j] for j in value] for value in dictionary.values()]
    import numpy as np
    b = np.array(a)
    c = np.sum((b/len(a)), axis=0)
    c = np.array([round(i, 1) for i in c])
    d = []
    for i in a:
        acum = 0
        for j in i:
            acum += j
        d.append(acum)
    mayor = max(d)
    idx = d.index(mayor)
    # p = list(dictionary.keys())
    p= [key for key in dictionary.keys() if mayor == sum(dictionary[key].values())]
    e = p[idx]
    d = np.array(d)
    return a, b, c, d, e

arqueros = {'Robin Hood': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Odiseo': {
 'prueba 1': 5, 'prueba 2': 7, 'prueba 3': 9}, 'Green Arrow': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}
a, b, c, d, e = reto_4(arqueros)
a = f"Resultados: {a}"
b = f"Matriz: \n{b}"
c = f"Promedio: {c}"
d = f"Puntajes: {d}"
e = f"Seleccionado: {e}"
print(a, b, c, d, e, sep='\n')

arqueros= {'Odiseo': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Hawk Eye': {
 'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Katniss': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}
a, b, c, d, e = reto_4(arqueros)
a = f"Resultados: {a}"
b = f"Matriz: \n{b}"
c = f"Promedio: {c}"
d = f"Puntajes: {d}"
e = f"Seleccionado: {e}"
print(a, b, c, d, e, sep='\n')

arqueros = {'Robin': {'prueba 1': 9, 'prueba 2': 9, 'prueba 3': 9}}
a, b, c, d, e = reto_4(arqueros)
a = f"Resultados: {a}"
b = f"Matriz: \n{b}"
c = f"Promedio: {c}"
d = f"Puntajes: {d}"
e = f"Seleccionado: {e}"
print(a, b, c, d, e, sep='\n')