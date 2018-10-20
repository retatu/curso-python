#Números são tipos de dados para armazenamento de números inteiros ou pontos flutuantes
#String são tipos de dados para armazenamento de conjuntos de caracteres
#Listas contem conjunto de váriáveis com tamanho variável, ou seja, pode ser adicionado outras variáveis
#Tupla é uma lista com tamanho fixo
#Diciários é um tipo para armazenamento de tipos onde a indexação é feita por uma chave

#Chegar no valor 100.25
a = 5**2*4+2.5/2-1
print(a)

b = 4*(6+5)
print(b)

c = 4*6+5
print(c)

d = 4+6*5
print(d)

#retorna um tipo flutuante

#Para encontrar a raiz quadrada é só fazer a exponenciação por 1/2, ja o quadrado é a exponenciação por 2
e = 2**(1/2)
print(e)
e = 2**2
print(e)

s = 'hello'
print(s[1])
print(s[::-1])
print(s[4:])
print(s[-1])

l = [1,2,[3,4,'hello']]
print(l)
l[2][2] = 'goodbye'
print(l)

l2 = [5,3,4,6,1]
l2.sort()
print(l2)


d = {'simple_key':'hello'}
print(d['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[1,2,{'k2':['this is tricky', {'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])


#Tuplas não possuem tamanhos variáveis, diferente das listas
#Para criar uma tupla em vez de utilizar colchetes, utiliza parenteses

#Quando não há mais de uma série de valores
s = [1,2,2,33,4,4,11,22,3,3,2]
print(set(s))


#false
#false
#false
#true
#false
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4**0.5 != 2)

#false
l1 = [1,2,[3,4]]
l2 = [1,2,{'k1':4}]
print(l1[2][0] >= l2[2]['k1'])
