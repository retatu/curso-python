def minha_funcao():
    """
    Doc da função, descrição...
    """
    print("Primeira função")

def soma(num1, num2):
    return (num1+num2)

def verifica_se_eh_primo(num):
    """
    Verifica se o número é primo
    """
    def divisivel (a, b):
        """
        retorna o resto da divisão
        """
        return a%b
    
    for i in range(2,num):
        if divisivel(num, i) == 0:
            print("Não é primo")
            break
    else:
        print("É primo")

minha_funcao()
x = soma(1,2)
print(x)
verifica_se_eh_primo(9)
