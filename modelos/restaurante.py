class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome.ljust(15)} | {self.categoria}'
    
    def __repr__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(15)}|{'Categoria'.ljust(15)}|{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)}|{restaurante._categoria.ljust(15)}|{restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_pizza = Restaurante('pizza Express','Italiana')

Restaurante.listar_restaurantes()
restaurante_pizza.alternar_estado()
Restaurante.listar_restaurantes()