from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_praca.receber_avaliacao('Roberto',10)
restaurante_praca.receber_avaliacao('Claudia',5)
restaurante_praca.receber_avaliacao('Fernando',7)
restaurante_praca.receber_avaliacao('Marcia',8)
restaurante_italiano = Restaurante('Mammamia','Italiano')

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()