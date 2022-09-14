from pickle import dump, load
from time import sleep
from pessoa import *
from pokemon import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada')

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            dump(player, arquivo)
            print('Jogo salvo com sucesso')            
    except Exception as error:
        print('Erro ao salvar jogo')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            load(arquivo)
            return player       
    except:
        print('\nSave não encontrado\n')

if __name__ == '__main__':
    print('-----------------------------------------')
    print('Bem vindo ao game Pokemon RPG de terminal')
    print('-----------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input('Olá, qual o seu nome?: ')
        player = Player(nome)
        print(f'Olá {player}, esse é um mundo habitado por pokemons. A partir de agora sua missão é se tornar um mestre dos pokemons.\n'
            'Capture o máximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemons
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um.')
            escolher_pokemon_inicial(player)

        print('Pronto, agora que você já possui um pokemon enfrente seu arqui-rival desde o jardim da infância, Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('---------------------------------')
        print('O que deseja fazer?\n'
              '1 - Explorar pelo mundo afora\n'
              '2 - Lutar com um inimigo\n'
              '3 - Ver Pokédex\n'
              '0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo: 3')
            sleep(1.2)
            print('Fechando o jogo: 2')
            sleep(1.2)
            print('Fechando o jogo: 1')
            sleep(1.2)
            print('Fechando o jogo: 0')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Escolha inválida')