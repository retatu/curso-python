meu_arquivo = open('arquivo/texto.txt')
print(meu_arquivo)
#le todo o arquivo e o cursor vai para o final
print(meu_arquivo.read())
#coloca o cursor na posição 0
print(meu_arquivo.seek(0))
#le a linha atual e vai para a próxima
print(meu_arquivo.readline())
meu_arquivo.seek(0)

for linha in meu_arquivo:
    print(linha)
