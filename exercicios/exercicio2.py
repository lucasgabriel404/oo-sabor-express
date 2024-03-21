class Carro:

    lista_carros = []

    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        Carro.lista_carros.append(self)

    def __str__(self):
        return f'{self.modelo},{self.cor},{self.ano}'
    
    def listar_carros():
        for carro in Carro.lista_carros:
            print(carro)

carro1 = Carro('Corsinha','Preto',1998)

Carro.listar_carros()