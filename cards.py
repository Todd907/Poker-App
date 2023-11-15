import random


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        value_name = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        suit_name = ["Spades", "Diamonds", "Clubs", "Hearts"]

        return f"{value_name[self.value]} of {suit_name[self.suit]}"
        
class StandardDeck(list):
    def __init__(self):
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(value, suit)) for suit in suits] for value in values]

    def shuffle(self):
        # print("Deck Shuffled")
        random.shuffle(self)

    def deal(self):
        if (len(self) > 0):
            # print(self.pop())
            return self.pop()
        else:
            return None
