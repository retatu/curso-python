lista = [1,2,4,2,4,7]
#Aplica um filtro sobre a lista e retorna quando for verdadeiro
x = list(filter(lambda x : x%2 == 0, lista))
print(x)
