class Livro(object):
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        print("Livro criado.")
    def __str__(self):
        return "Titulo do livro {a}".format(a=self.titulo)
    def __len__(self):
        return self.paginas
    def __del__(self):
        print("Deletado")

livro = Livro("Titulo", "Matheus", 4)
print(livro)
print(len(livro))
del livro
