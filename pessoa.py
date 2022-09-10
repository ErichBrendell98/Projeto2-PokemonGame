from pokemon import *
import random

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
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem pokemon')


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


meu_inimigo = Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemons()