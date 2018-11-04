def funcao():
    nome = 'Matheus'
    print(locals())

def ola(nome = 'Matheus'):
    print("Oi, matheus")

    def tudo_bem():
        print("Tudo bem, ",nome)

    def tchau():
        print("Tchau, ",nome)

    print(locals())
    
    if nome == "Matheus":
        return tudo_bem
    else:
        return tchau

def funcao_externa(func):
    '''Recebe uma função por parámetro e a chamas'''
    print("Função Externa")
    func()
    print("Outra função chamada: ", locals()['func'])

def funcao_interna():
    print("Função Interna")


def novo_decorador(func):
    def funcao_interna():
        print("Função interna executada, executando função passada por parâmetro...")
        func()
        print("Ok...")
    return funcao_interna

#COm essa anotação, o python já faz a função de decorar a função
@novo_decorador
def funcao_para_decorar():
    print("Essa função será decorada.")

a = "Variavel global"
print(globals()['a'])
print()
print(locals())
print()

funcao()
copia_funcao = funcao
del funcao
copia_funcao()

print()

ola()
#Recebe o retorno da função que ola retornará
tchau = ola("Mateus")
tchau()

print()

#Função externa chamará o método interno
funcao_externa(funcao_interna)

print()

novo_decorador(funcao_interna)()

print()

funcao_para_decorar()
