def calcula(v):
    return v**2

lista = [1,5,3,2]
for i in lista:
    print(calcula(i))

#Map aplica a instrução para os iteráveis
print(list(map(calcula, lista)))
print(list(map (lambda v : v**0.5, lista)))
