x = 0;
y = 0;
while(x < 15 and y < 15):
    if(x > y):
        y += x
    x+= 1
    print("X: ",x," Y: ",y)

x = 0
while True:
    x += 1
    if x > 10:
        break
print(x)
x = 0
while x < 10:
    x += 1
    if x%2 == 1:
        continue
    else:
        print(x)

