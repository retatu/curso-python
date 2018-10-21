lista = [i for i in range(0,10,2)]
print(lista)

lista = [i * 2 for i in range(0,10,2)]
print(lista)

#com if após o for, vai depois do for
lista = [i * 3 for i in range(0,10) if i%2 != 0]
print (lista)

lista2 = [i for i in "teste"]
print(lista2)

celsius = [0,10,20,25]
fahrenheit = [i * (9/5) + 32 for i in celsius]
print(celsius)
print(fahrenheit)
