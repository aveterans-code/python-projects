#ch10ex11.py
    #Testing card class

import time, math

class Card():
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suit

    def value(self):
        if self.getRank() < 10:
            return self._rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four",
                 "Five", "Six", "Seven", "Eight",
                 "Nine", "Ten", "Jack", "Queen", "King"]

        if self._suit == 'c':
            suitStr = "Clubs"
        elif self._suit == "d":
            suitStr = "Diamonds"
        elif self._suit == "h":
            suitStr = "Hearts"
        else:
            suitStr = "Spades"
        return f"{ranks[self._rank]} of {suitStr}"

from random import randrange

def main():
    print("Testing card class\n")
    n = int(input("Number of cards to see? "))

    for i in range(n):
        rank = randrange(1, 14)
        suit = "dchs"[randrange(4)]
        randCard = Card(rank, suit)

        print(f"The card: {randCard} - Blackjack value: {randCard.value()}")

if __name__ == '__main__':
    main()        
