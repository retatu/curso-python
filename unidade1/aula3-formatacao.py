s = 'Valor'
valor1 = 1.45
valor2 = 4
print(s)
#printar no meis de outra string utilizado o método str()
print('Aqui tem um %s de alguma coisa' %(s))
#também apresenta a string utilizando o método repr()
print('Aqui tem um %r de alguma coisa' %(s))

#o 5 ante o .2f representa a quantidade de espaços antes de printar
print('valores: %s double %10.2f, integer %r' %(s, valor1, valor2))

#método format
s = 'V1: {a}, V2: {b} V3: {c}'.format(a=1.33, b=2, c='string')
print(s)
