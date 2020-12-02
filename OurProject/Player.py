from OurProject.Deckofcards import Deckofcards
from OurProject.Card import Card
import random


class Player:
    def __init__(self, name, pack=10):
        self.name = name
        self.pack = []

    def __str__(self):
        return f'{self.name} have the package {self.pack}'

    def show(self):
        return f'{self.name} have the package {self.pack}'

    def set_hand(self, deck, cardsnum):
        for i in range(0, cardsnum):
            self.pack.append(deck.pop(i))
        return self.pack

    def get_random_card(self):
        packlen = len(self.pack)
        randnum = random.randint(0, packlen-1)
        return self.pack.pop(randnum)

    def add_card(self, newcard):
        kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
        x= kind[newcard.suit]
        self.pack.append((newcard.value, kind[newcard.suit]))
        return