def reto_5(ruta_archivo: str) -> list:
    import numpy as np
    import pandas as pd
    document = pd.read_csv(ruta_archivo)
    document['PUNTAJE'] = document['MATEMATICA'] + document['LENGUAJE'] + document['CIENCIAS'] + document['CIUDADANAS'] + document['IDIOMAS']
    qual = document.sort_values('PUNTAJE', ascending=False).head()
    tabla_1 = qual[['ESTUDIANTE', 'PUNTAJE']]
    placement = [1,2,3,4,5]
    tabla_1 = tabla_1.set_index(np.array(placement))
    tabla_1.index.name = 'PUESTO'
    media = document.mean()
    media = media.round(2)
    tabla_2 = pd.DataFrame(media)
    tabla_2.columns = ['PROMEDIO']
    tabla_2.index.name = 'PRUEBAS'
    return tabla_1, tabla_2

top, promedio = reto_5('resultados.csv')
print('Tabla 1:\n', top)
print('\nTabla 2:\n', promedio)