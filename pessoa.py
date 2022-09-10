import random

from pokemon import *

NOMES = [
    'João', 'Isabela', 'Lorena', 'Francisco', 'Ricardo', 'Diego',
    'Patrícia', 'Marcelo', 'Gustavo', 'Gerônimo', 'Gary'
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('Charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonAgua('Squartle'),
    PokemonAgua('Magicarp'),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]) -> None:
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self) -> str:
        return self.nome    

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for index, pokemon in enumerate(self.pokemons):
                print(f'{index} - {pokemon}')
        else:
            print(f'{self} não tem nenhum pokemon')

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('Escolha o seu pokemon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} eu escolho você!!!')
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon para ser escolhido')

    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pessoa.escolher_pokemon()

        self.escolher_pokemon()


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')


class Inimigo(Pessoa):
    tipo = 'inimigo'
    
    def __init__(self, nome=None, pokemons=[]) -> None:
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon para ser escolhido')
