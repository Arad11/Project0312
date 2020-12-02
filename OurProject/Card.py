class Card:
    def __init__(self, value, suitID):
        self.value = value
        kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
        self.suit = kind[suitID]

    def show(self):
        kind = {1: 'diamond', 2: 'spade', 3: 'heart', 4: 'club'}
        return f'the card value is {self.value} \nthe suit is {kind[self.suit]}'
    def __repr__(self):
        return  f'{self.value, self.suit}'


    def war(self, card1, *args):
        if self.value == 1:
            maxvalue = self.value
            maxsuit = self.suit
        elif card1.value == 1:
            maxvalue = card1.value
            maxsuit = card1.suit
        elif self.value < card1.value:
            maxvalue = card1.value
            maxsuit = card1.suit
        elif self.value > card1.value:
            maxvalue = self.value
            maxsuit = self.suit
        elif self.value == card1.value:
            if self.suit > card1.suit:
                maxvalue = self.value
                maxsuit = self.suit
            else:
                maxvalue = card1.value
                maxsuit = card1.suit

        for i in range(len(args)):
            if maxvalue < args[i].value:
                maxvalue = args[i].value()
                maxsuit = args[i].suit
            elif args[i].value == 1:
                maxvalue = args[i].value
                maxsuit = args[i].suit
            elif args[i].value == maxvalue:
                if self.suit < args[i].suit:
                    maxvalue = args[i].value
                    maxsuit = args[i].suit

        if maxvalue == self.value and maxsuit == self.suit:
            return True
        else:
            return False