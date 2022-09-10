from pokemon import *
import random

NOMES = [
        'João', 'Isabela', 'Lorena', 'Francisco', 'Ricardo', 'Diego',
        'Patrícia', 'Marcelo', 'Gustavo', 'Gerônimo', 'Gary'
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
    


eu = Player()

print(eu)