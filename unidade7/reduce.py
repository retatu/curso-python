from functools import reduce

lista = [1,2,4,2,4,7]
x = reduce(lambda x,y: x+y, lista)
print(x)

x = reduce(lambda x,y : x if(x>y) else y, lista)
print(x)
