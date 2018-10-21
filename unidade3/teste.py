vol = lambda raio: 3/4*3.14*(raio**3)
print(vol(3))

rank_check = lambda n, low, high: n < high and n > low
print(rank_check(5,3,10))

def up_low(s):
    u = 0
    l = 0
    for letra in s:
        if letra.isupper():
            u+=1
        elif letra.islower():
            l+=1
    return (u,l)
print(up_low("OOOOIIII aaa"))

def unique_list(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista
print(unique_list([2,1,1,2,3,4,3,5,2]))

def multiply(numbers):
    x = 1;
    for i in numbers:
        x *= i
    return x
print(multiply([1,2,3,-4]))

def palindrome(s):
    aux = s[::-1]
    return s == aux
print(palindrome("helleh"))


import string
def ispangram(s):
    alphabet = string.ascii_lowercase
    aux = True
    for vlr in alphabet:
        if vlr in s:
            continue
        else:
            aux = False
            break
    return aux
print(ispangram("asdfkjahsgf"))

