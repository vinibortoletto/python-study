from collections.abc import Iterable, Iterator
from typing import Iterator


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return "<%s de %s>" % (self.valor, self.naipe)


class IteratorDoBaralho(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._posicao = 0

    def __next__(self):
        try:
            carta = self._cartas[self._posicao]
        except IndexError:
            raise StopIteration
        else:
            self._posicao += 1
            return carta


class IteratorDoBaralhoInverso(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._posicao = -1

    def __next__(self):
        try:
            carta = self._cartas[self._posicao]
        except IndexError:
            raise StopIteration()
        else:
            self._posicao -= 1
            return carta


class Baralho(Iterable):
    naipes = "copas ouros espadas paus".split()
    valores = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe) for naipe in self.naipes for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return IteratorDoBaralhoInverso(self._cartas)

    def __str__(self):
        return f"{[carta for carta in self]}"


baralho = Baralho()
for carta in baralho:
    print(carta)
