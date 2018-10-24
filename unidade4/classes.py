class PrimeiraClasse(object):
    pass

class Dog(object):
    especie = "Mamífero"
    def __init__(self, raca):
        self.raca = raca

x = PrimeiraClasse()
print(type(x))

pipoca = Dog(raca="Cusco")
print(type(pipoca))
print("Raça da pipoca: "+pipoca.raca)
print("Espécie da pipoca: "+pipoca.especie)
