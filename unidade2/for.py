l = [1,5,6,7,2,4,1,6,8,9]
somatorio = 0;
for val in l:
    somatorio += val;
    if val%2 == 0:
        print('O valor ', val, 'é par')
    else:
        print('O valor', val, 'é impar')

print('Somatório dos valores é: ',somatorio)

string = "Valor na String"

for val in string:
    print(val)

tupla = (1,6,7,3,1,2)
for val in tupla:
    print(val)

l = [(1,2), (2,3), (3,4)]

(t1, t2) = l[0]

print(t1 * t2)
print("Iterando nas tuplas da lista")
for (t1, t2) in l:
    print (t1, t2)

print("Itenrando nos dicionários")

d = {'k1':1, 'k2':2, 'k3':3}
for (key, valor) in d.items():
    print(key, ':', valor)
