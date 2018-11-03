from functools import reduce

def word_lengths(string):
    return list(map(lambda s : len(s), string.split(" ")))

def digits_to_num(lista):
    return int(reduce(lambda x,y: x+y, lista))

def filter_words(lista, letra):
    return list(filter(lambda s : s[0] == letra, lista))

def concatenate(lista1, lista2, cancatenador):
    return [l1+cancatenador+l2 for (l1,l2) in zip(lista1,lista2)]

def d_list(lista):
    return {key:value for value, key in enumerate(lista)}

def cout_match_index(lista):
    return len([num for count, num in enumerate(lista) if num == count])

    
print(word_lengths(" sd sd sdf asd"))
print(digits_to_num([1,2,4,2,4,7]))
print(filter_words(["qw","dfg","dfadg","asad"], 'd'))
print(concatenate(["a","b"], ["A","B"], "-"))
print(d_list(["a","b"]))
print(cout_match_index([1,2,3,3,3,5,6,4,3,6,7]))
