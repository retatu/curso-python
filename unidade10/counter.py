from collections import Counter
l = [1,2,3,5,2,1,3,5,6,4,2]
print(Counter(l))
print(Counter('fdsfhsuidhfshdf'))
s = 'Quantas palavras existem aqui aqui'
c = Counter(s.split())
print(c)
print()
#as tres mais comum...
print(c.most_common(3))
#contagem
print(c.values())
print(list(c))
print(c.items())
