class Pessoa:
    def __init__(self, nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'O nome da pessoa é {self.nome}, {self.idade} anos, e trabalha como {self.profissao}'
    
    def aumentar_idade(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Bem vindo, {self.nome}, ao setor de {self.profissao}s'
        else:
            return f'Bem vindo, {self.nome}'

lucas = Pessoa('Lucas',28,'Analista')

print(lucas)

lucas.aumentar_idade()

print(lucas)

print(lucas.saudacao)