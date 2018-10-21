st = "Print only the words that start with s in this sentence"
lista = st.split(" ");
for vlr in lista:
    if(vlr[0] == 's'):
        print(vlr)

print(list(range(0,10,2)))

lista = [i for i in range(1,50) if i % 3 == 0]
print(lista)

st = "Print every word in this sentence that has an even number of letters"
for i in st.split():
    if len(i)%2 == 0:
        print(i)

lista = range(0,100)
for vlr in lista:
    if vlr % 5 and vlr % 3:
        print("FizzBuzz")
    elif vlr % 3 == 0:
        print("Fizz")
    elif vlr % 5 == 0:
        print("Buzz")
    
st = "Create a lista of the first letters of every word in this string"
lista = [i[0] for i in st.split()]
print(lista)
