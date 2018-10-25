def ask():
    erro = 0
    while True:
        try:
            n = int(input("Digite um número: "))
            print("Seu número é: ")
            print("Ao quadrado é: ",n**2)
        except:
            erro += 1
        finally:
            print("Ate o momento, ocorreu : ", erro," erros")


try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Erro ao realizar a operaçao")

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Não é possivel realizar a divisão por zero")


ask()
