class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}!'


if __name__ == '__main__':
    p = Pessoa('José', 28)
    print(p.cumprimentar())
