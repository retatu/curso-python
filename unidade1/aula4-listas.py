#Listas possuem tamanhos dinâmicos em python
minha_lista = [1, 2, 3, 7, 7, 2]
print(type(minha_lista))
print(len(minha_lista))
print(minha_lista)
minha_lista2 = [1, 2, 1.3, "String"]
print(minha_lista2)
print(minha_lista2[1])
print(minha_lista2[1:3])
print(minha_lista2[::-1])

minha_lista2 = minha_lista2 + minha_lista + ['novo valor']
print(minha_lista2)

print(minha_lista * 3)

#Adiciona um novo elemento
minha_lista2.append('Novo elemento')

#remove o ultimo elemento, igual uma pilha. Se passar o index vai remover o valor naquele index
print(minha_lista2.pop())
print(minha_lista2.pop(2))

#Reverse inverte os valores da lista permanentemente
minha_lista.reverse()
print(minha_lista)
#Ordena a lita
minha_lista.sort()
print(minha_lista)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
matriz = [lista1, lista2, lista3]
print(matriz)
print(matriz[2])
print(matriz[2][1])
