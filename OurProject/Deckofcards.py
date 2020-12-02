import random
from OurProject.Card import Card


class Deckofcards:
    def __init__(self, sumcards=13):
        self.diamond = {}
        self.spade = {}
        self.heart = {}
        self.club = {}
        self.package = []
        for i in range(1, 14):
            self.diamond.update({i: 'diamond'})
        self.package += self.diamond.items()
        for i in range(1, 14):
            self.spade.update({i: 'spade'})
        self.package += self.spade.items()
        for i in range(1, 14):
            self.heart.update({i: 'heart'})
        self.package += self.heart.items()
        for i in range(1, 14):
            self.club.update({i: 'club'})
        self.package += self.club.items()

    def __str__(self):
        return f"the package is {self.package}"

    def suffle_the_pack(self):
        random.shuffle(self.package)
        return self.package

    def deal_one(self):
        random.shuffle(self.package)
        randnum = random.randint(0, len(self.package) - 1)
        return self.package.pop(randnum)

    def show(self):
        return f"the package is {self.package}"