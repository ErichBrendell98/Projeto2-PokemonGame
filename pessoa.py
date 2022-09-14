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

    def __init__(self, nome=None, pokemons=[], dinheiro=100) -> None:
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

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
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon para ser escolhido')

    def mostrar_dinheiro(self):
        print(f'Você possui $ {self.dinheiro} em sua conta')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'Você ganhou $ {quantidade}')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha')
                    break

        else:
            print('Essa batalha não pode ocorrer.')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')

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

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'Um pokemon selvagem apareceu: {pokemon}')
            
            escolha = input('Deseja capturar o pokemon(s/n)?: ')
            
            if escolha in 'sS':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f'{pokemon} fugiu!!! Que pena...')
            elif escolha in 'nN':
                print('Ok, boa viagem')
        else:
            print('Essa exploração não deu em nada...')


class Inimigo(Pessoa):
    tipo = 'inimigo'
    
    def __init__(self, nome=None, pokemons=[]) -> None:
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

