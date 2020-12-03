from OurProject.Card import Card
from OurProject.Player import Player
import random
from OurProject.Deckofcards import Deckofcards
from OurProject.CardGame import CardGame

cplayer=0

c = CardGame("Nitzan", "Arad")
print(c.player1.show())
print(c.player2.show())
for i in range(1, 10):
    lst1=list(c.player1.get_random_card())
    lst2=list(c.player1.get_random_card())
    kind = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
    card1=Card(lst1[0], lst1[1])
    card2=Card(lst2[0], lst2[1])
    print(f"round {i+1} \nthe cards whict droped are: \n {card1.show()} \n {card2.show()}")
    if card1.war(card2) == True:
        cplayer += 1
        c.player1.add_card(card1)
        c.player1.add_card(card2)
        print(f"the winner in this round is {c.player1.name}\n\n")
    else:
        print(f"the winner in this round is {c.player2.name}\n\n")
        c.player2.add_card(card1)
        c.player2.add_card(card2)

if cplayer > 5:
    print(f'{c.player1.name} is the winner')
elif cplayer < 5:
    print(f'{c.player2.name} is the winner')
else:
    print("even")
