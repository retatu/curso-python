import random

def printa_tabuleiro (lista):
    for i in lista:
        print(i)

def realiza_jogada(i, j, jogador, lista):
    print("Jogada realizada!")
    lista[i][j] = jogador

def verifica_ganhador(lista):
    for i in lista:
        if i[0] == i[1] == i[2] and i[0] != 0:
            return True
    for i in range(0,2):
        if lista[0][i] == lista[1][i] == lista[2][i] and lista[0][i] != 0:
            return True
    if lista[0][0] == lista[1][1] == lista[2][2] and lista[0][0] != 0:
        return True
    if lista[0][2] == lista[1][1] == lista[2][0] and lista[0][2] != 0:
        return True
    return False

verifica_posicao = lambda i, j, lista : lista[i][j] != 0

def computador_joga(lista):
    x = random.randint(0,2)
    y = random.randint(0,2)
    while verifica_posicao(x,y,lista):
        x = random.randint(0,2)
        y = random.randint(0,2)
    else:
        realiza_jogada(x, y, 2, tabuleiro)


print("Bem vindo ao jogo da velha")
tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
print(verifica_ganhador(tabuleiro))
while not verifica_ganhador(tabuleiro):
    printa_tabuleiro(tabuleiro)
    print("Digite o x: ")
    x = int(input())
    print("Digite o y: ")
    y = int(input())
    while verifica_posicao(x,y,tabuleiro):
        print("Posição já ocupada, por favor escolha outra.")
        print("Digite o x: ")
        x = int(input())
        print("Digite o y: ")
        y = int(input())
    realiza_jogada(x, y, 1, tabuleiro)
    printa_tabuleiro(tabuleiro)
    if not verifica_ganhador(tabuleiro):
        computador_joga(tabuleiro)
        if verifica_ganhador(tabuleiro):
            print("Computador ganhou.")
    else:
        print("Você ganhou.")
