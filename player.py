# Project: player
# Author: Chris Diewtragulchai

class Player(object):
    def __init__(self):
        # List variable to keep track of what is in the player's hand
        self.Hand = []
        # Bool Variable to track whether or not an ace is in the hand
        self.Ace = False
        # A variable to track the amount of aces in the player's hand
        self.AceAmount = 0;
        # A variable to track the value of the player's hand, not accounting the ace
        self.Value = 0

    # A function to print out both the player's hand and its value
    def printHand(self):
        print("Your Hand: ")
        for i in range(len(self.Hand)):
            print(self.Hand[i])

        print("The Value of your Hand: " + str(self.getValue()))

    # A function to add a card to the player's hand and record it's value
    def addCard(self, cardType, cardValue):
        self.Hand.append(cardType)

        # If the index(cardValue) is 0 then it is an Ace and the bool flag is tripped and a 1 is added to the AceAmount
        if cardValue == 0:
            self.Ace = True
            self.AceAmount += 1
        # If the index is for a 10 or higher than add a 10
        elif cardValue > 9:
            self.Value += 10
        # Otherwise add 1 to the index since the index is 1 lower than the cards actual value
        else:
            self.Value += cardValue + 1

    # A function that returns the value of hand and accounts for the value of an Ace
    def getValue(self):
        temp = self.Value

        if self.Ace:
            for i in range(self.AceAmount):
                if temp + 11 > 21:
                    temp += 1
                else:
                    temp += 11
        return temp

    # A function to clear the list tracking the hand and resetting the Ace Variable
    def resetHand(self):
        self.Hand.clear()
        self.Ace = False
        self.AceAmount = 0
        self.Value = 0

    # A function to check whether or not the player busted by getting a hand value greater than 21
    def checkBust(self):
        if self.getValue() < 21:
            return False
        else:
            return True
