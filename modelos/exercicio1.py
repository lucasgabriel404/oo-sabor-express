class Restaurante:
    nome = ''
    categoria = 'whatever'
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome='Bistrô'
restaurante_praca.categoria='Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Palace'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

restaurantes = [restaurante_pizza,restaurante_praca]

categoria = Restaurante.categoria

print(vars(restaurante_praca))

if not restaurante_praca.ativo:
    print('Restaurante Inativo.')

else:
    print('Restaurante Ativo.')

if restaurante_pizza.categoria == 'Fast Food':
    print('É fastfood.')
else:
    print('Não é fastfood.')

print(categoria)

print(f'Nome: {restaurante_praca.nome}, Categoria:{restaurante_praca.categoria}')
