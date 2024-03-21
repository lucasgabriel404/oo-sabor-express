from exercicios.livro import Livro

livro1 = Livro('Joan', ' Robertson', 2013)

livro1.emprestar()

print(livro1._disponivel)

livro1.emprestar()

Livro.verificar_disponibilidade(2013)

