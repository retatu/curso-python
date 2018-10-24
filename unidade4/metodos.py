class Dog(object):
    especie = "Mamífero"
    def __init__(self, raca):
        self.raca = raca
    def latir(self):
        print("Au Au!")

class Circulo(object):
    pi = 3.14
    def __init__(self, raio=1):
        self.raio = raio
    def defRaio(self, raio):
        self.raio = raio
    area = lambda self : self.raio ** 2 * self.pi
    getRaio = lambda self : self.raio
    

pipoca = Dog(raca="Cusco")
print(type(pipoca))
print("Raça da pipoca: "+pipoca.raca)
print("Espécie da pipoca: "+pipoca.especie)
pipoca.latir()


circulo = Circulo(2)
print(circulo.area())
print(circulo.getRaio())
circulo.defRaio(3)
print(circulo.area())
print(circulo.getRaio())
