#dentro do set, haverá apenas valores únicos e estarão de forma ordenada
#set nao permite listas
meu_set = set()
print(type(meu_set))
print(meu_set)
meu_set.add(1)
meu_set.add(5)
meu_set.add(1)
meu_set.add(3)
meu_set.add('valor')
print(meu_set)

lista = [1,1,1,2,3,4,5,34,3,2,8,7,6,9,2,3,5,1,9,0,7,9]
print('lista : %s' %(lista))
print('no set :%s' %(set(lista)))
