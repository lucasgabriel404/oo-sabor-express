from exercicios.livro import Livro

livro1 = Livro('LIVRO DA VIDA','VIDA', 236)
livro2 = Livro('LIVRO DA MORTE','MORTE', 7844)





def main():
    print(livro1)
    print(livro2)

    Livro.listar_livros()
    


if __name__ == '__main__':
    main()