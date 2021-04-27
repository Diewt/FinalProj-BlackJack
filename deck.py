# Project: deck
# Author: Chris Diewtragulchai

import random


# deck class to keep track of the 52 card deck
class Deck(object):
    def __init__(self):
        # constant variable for the amount of each type of card in the deck
        self.StandardAmount = 4
        # list that keeps track of the amount of each card left in the deck
        self.CardCount = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    # function to check if the random card type is still available in the deck
    def draw(self):
        draw = random.randint(0, 12)

        while self.CardCount[draw] == 0:
            draw = random.randint(0, 12)

        self.CardCount[draw] -= 1
        return draw

    # function to reset the deck
    def reshuffle(self):
        for i in range(len(self.CardCount)):
            self.CardCount[i] = self.StandardAmount

    # function to return the amount of cards left in the deck
    def totalCards(self):
        total = 0
        for i in range(len(self.CardCount)):
            total += self.CardCount[i]

        return total
