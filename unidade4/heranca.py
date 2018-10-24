class Animal(object):
    def __init__(self):
        print("Animal Criado")
    def quemSouEu(self):
        print("Sou um animal")
    def comer(self):
        print("Comendo...")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro criado")
    quemSouEu = lambda self : print("Sou um cachorro")
    latir = lambda self : print("Au Au")

animal1 = Animal()
animal1.quemSouEu()
animal1.comer()
print("---------")

cachorro = Cachorro()
cachorro.quemSouEu()
#Comer é da classe animal..
cachorro.comer()
cachorro.latir()
