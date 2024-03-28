class ContaBancaria:
    def __init__(self,titular='',saldo=0):
        self._titular=titular
        self._saldo=saldo
        self._ativo=False

    def __str__(self):
        return f'Bom dia, {self.titular}, seu saldo é de {self.saldo} reais! Status:{self.ativo}'
    
    @classmethod
    def ativar_conta(cls,conta):
        conta._ativo = not conta._ativo

    @classmethod
    def criar_conta(cls,titular,saldo):
        conta = ContaBancaria(titular,saldo)
        return conta

    @property
    def ativo(self):
        return f'Ativo' if self._ativo else 'Desativo'
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
pessoa1 = ContaBancaria(titular = 'Lucas Gabriel',saldo = 554785)
pessoa2 = ContaBancaria(titular = 'Gabriel dos Santos', saldo = 5478)

pessoa3 = ContaBancaria.criar_conta('Gary',20)

print(pessoa1)
print(pessoa2)
print(pessoa3)
ContaBancaria.ativar_conta(pessoa1)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa1.titular)