class Livro:

    lista_livros = []

    def __init__(self,titulo,autor,ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
            return f'{self._titulo} foi escrito por {self._autor} no ano de {self._ano_publicacao}.\n'

    def listar_livros():
        for livro in Livro.lista_livros:
             print(livro)

    def emprestar(self):
        self._disponivel = not self._disponivel
        status = 'Disponível' if self._disponivel == True else 'Indisponível'
        print(f'O livro {self._titulo} está {status}\n')

    def verificar_disponibilidade(ano):
        for livro in Livro.lista_livros:
            if livro._ano_publicacao == ano:
                 print('Segue lista de livros publicados neste ano:\n', livro)
            

livro1 = Livro('Hobbit', 'Tolkien', 1950)
livro2 = Livro('Orgulho e Preconceito','Jane Austin', 1800)

Livro.listar_livros()

livro1.emprestar()
livro1.emprestar()


Livro.verificar_disponibilidade(1800)