class Musica:

    lista_musicas = []

    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.lista_musicas.append(self)

    def __str__(self):
        return f'{self.artista} - {self.nome}, {self.duracao} segundos.'

    def listar_musicas():
        for musica in Musica.lista_musicas:
            print(musica)


musica1 = Musica('Bohemian Rhapsody','Queen',355)
musica2 = Musica('Imagine','John Lennon',183)
musica3 = Musica('Shape of You','Ed Sheeran',234)

Musica.listar_musicas()
