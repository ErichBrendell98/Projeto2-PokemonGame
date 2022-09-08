class Pokemon:

    def __init__(self, especie, level=1, nome=None) -> None:
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie


    def __str__(self) -> str:
        return f'{self.nome} ({self.level})'


    def atacar(self, pokemon):
        print(f'{self.nome} atacou {pokemon.nome}')


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print(f'{self} lançou um raio do trovão em {pokemon}')


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo em {pokemon}')


class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de agua em {pokemon}')


meu_pokemon = PokemonFogo('Charmander')
amigo_pokemon = PokemonEletrico('Pikachu')

print(meu_pokemon, meu_pokemon.tipo)
print(amigo_pokemon, amigo_pokemon.tipo)

meu_pokemon.atacar(amigo_pokemon)
amigo_pokemon.atacar(meu_pokemon)