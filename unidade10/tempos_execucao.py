import timeit

valores = '-'.join(str(n) for n in range(100))

print(valores)

t = timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000)
print(t)

t = timeit.timeit('"-".join([str(n) for n in range(100)])', number = 10000)
print(t)

t = timeit.timeit('"-".join(map(str, range(100)))', number = 10000)
print(t)
