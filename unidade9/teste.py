import random

def gen_squares(n):
    for i in range(n):
        yield i**2

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

print(list(gen_squares(5)))
print(list(rand_num(1,10,15)))
string = "Hello"
print(list(iter(string)))
#Quando é necesário gerar grandes volumes de dados
