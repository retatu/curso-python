meu_dicionario = {'chave1':'valor1', 'chave2':1.3, 'chave3':1, 'chave4':[1,2,[[1,2],[3,4]],4]}
print(type(meu_dicionario))
print(meu_dicionario)
print(meu_dicionario['chave2'])

print(meu_dicionario['chave1'][:3].upper())
print(meu_dicionario['chave4'][2][1][1])
meu_dicionario['chave4'] = 1
print(meu_dicionario)

meu_dicionario2 = {}
print(meu_dicionario2)
meu_dicionario2['chave1'] = 'valor1'
meu_dicionario2['chave2'] = 'valor2'
print(meu_dicionario2)

#Dicionario dentro de dicionário
meu_dicionario2['chave3'] = {'chave1':'valor1', 'chave2':'valor2'}
print(meu_dicionario2)

#retorna as chaves
print(meu_dicionario2.keys())
#retorna as chaves em formato de lista
print(list(meu_dicionario2.keys()))

#retorna os valores
print(meu_dicionario2.values())
#retorna os valors em formato de lista
print(list(meu_dicionario2.values()))

#retorna os valores dentro do dicionario
print(meu_dicionario2.items())
