catalogue = {}
# print(type(catalogue))

catalogue["Movies"] = ["Action", "Adventure", "Comedy", "Drama"]
# print(catalogue)
# print(catalogue.keys())
# print(catalogue.values())
# print(catalogue.items())

genres = catalogue["Movies"]
# print(genres)
genres_dic = dict.fromkeys(genres)
# print(genres_dic)
catalogue["Movies"] = genres_dic
# print(catalogue)

catalogue.update({"Series":{}, "Documentary":{}})

#Creando un nuevo diccionario
#El diccionario tiene 3 llaves que son diccionarios a su vez
catalogue_v2 = {'Movies': {'Action': None, 
                            'Adventure': None, 
                            'Comedy': None, 
                            'Drama': None}, 
                'Series': {}, 
                'Documentary': {}}

#Asignando la misma lista de géneros a series
# Forma 1
# catalogue_v2['Series'] = catalogue_v2['Movies']

#Forma 2
catalogue_v2['Series'] = genres_dic

#Crea una llave y le asigna una lista de valores
catalogue_v2['Documentary']['Animals'] = ['The bees', 'Wild life']
#Adicionando los mismos géneros a documentales.
catalogue_v2['Documentary'].update(genres_dic)

#LLenando el diccionario series, llave aventura
catalogue_v2['Series']['Adventure'] = ['Serie 1', 'Serie 2', 'Serie 3']
for formato in catalogue_v2:
    print('formato', formato)
    for genero, formato in catalogue_v2[formato].items():
        print(f'Género:{genero} -> {formato}')

print(catalogue_v2)

# catalogo={}
# #print(type(catalogo))
# catalogo["peliculas"]=['accion','aventura','comedia','drama']
# # print(catalogo)
# # print(catalogo.keys())
# # print(catalogo.items())
# generos = catalogo["peliculas"]
# #print(generos)
# generos_dic = dict.fromkeys(generos)
# #print(generos_dic)
# #print(catalogo)
# catalogo["peliculas"] = generos_dic
# #print()
# #catalogo.update({'series':{}, 'documentales':{}})
# #print(catalogo)
# catalogo_v2 ={'peliculas': {'accion': None,
#                             'aventura': None, 
#                             'comedia': None, 
#                             'drama': None}, 
#                 'series': {}, 
#                 'documentales': {}
#             }
# catalogo_v2['series']= catalogo_v2['peliculas'].copy()
# #print(catalogo_v2)
# catalogo_v2['documentales'] ['animales']= ['las avispas','wiis life'] 
# # print(catalogo_v2)
# catalogo_v2['documentales'].update(catalogo_v2['peliculas'])
# print(catalogo_v2)