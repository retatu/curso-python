num = 1024
print(hex(num))
print(bin(num))
print(round(5.2322, 2))

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
s = 'wqwer2rqwersfsadfqwerfgetqwczxca'
print(s.count('w'))

s1 = {2,3,1,5,6,8}
s2 = {3,1,7,5,6,8}
print(s1.difference(s2))
print(s1.union(s2))

d={x:x**3 for x in range(5)}
print(d)

l1 = [1,2,3,4]
l1.reverse()
l2 = [2,3,1,5,6,3]
l2.sort()
print(l2)
