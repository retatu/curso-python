funcao_lambda = lambda : print("Exemplos função lambda")
funcao_lambda()

par = lambda s : s % 2 == 0
print(par(2))
print(par(3))

n1_maior_n2 = lambda n1, n2: n1 > n2
print(n1_maior_n2(1,2))
print(n1_maior_n2(4,2))

inverte_string_upper = lambda s : s[::-1].upper()
print(inverte_string_upper('String'))
