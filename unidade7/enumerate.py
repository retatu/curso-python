lista = ['a',('ba', 'bb'),'c','d']
print(list(enumerate(lista)))
#Altera a lista para ser uma lista de tupla e adiciona um contador no elemento da tupla
for number, item in enumerate(lista):
    print(number, " ", item)
