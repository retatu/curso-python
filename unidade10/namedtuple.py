from collections import namedtuple
teste = namedtuple('Tipo', 'valor1 valor2 valor3')
t1 = teste(valor1 = 'A1', valor2 = 'A2', valor3 = 'A3')
print(t1)
print(t1.valor2)
print(t1[0])
