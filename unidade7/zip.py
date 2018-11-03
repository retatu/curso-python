lista = [1,2,3,4,2,1,5,6]
lista2 = [1,2,53,4,2,3,5,6]
lista3 = list(zip(lista, lista2))
print(lista3)
lista4 = [12,1,3]
print(list(zip(lista,lista4)))
dicionario = {'a':2, 'b':3, '1':'a'}
dicionario2 = {'c':2, 'd':3, '2':'a'}
print(dict(zip(dicionario, dicionario2)))
print(list(zip(dicionario, dicionario2.values())))
