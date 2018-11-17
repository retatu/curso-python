def gen_cubes(i):
    for num in range(i):
        yield num**3

def gen_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

print(list(gen_cubes(10)))
print(list(gen_fib(15)))
g = gen_fib(15)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

string = "Teste"
string_iter = iter(string)
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
