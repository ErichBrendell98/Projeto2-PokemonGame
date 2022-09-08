from pokemon import *


class Pessoa:

    def __init__(self, nome=None, pokemons=[]) -> None:
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"

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

eu = Player('Erich')

pokemon_selvagem = PokemonFogo('Charmander')

print('Antes de capturar')
eu.mostrar_pokemons()

eu.capturar(pokemon_selvagem)
print('Depois de capturar')
eu.mostrar_pokemons()