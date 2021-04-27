# Project: blackjack
# Author: Chris Diewtragulchai

from deck import Deck
from player import Player
from dealer import Dealer

class Blackjack(object):
    def __init__(self):
        # Declaration of the Deck variable in the class
        self.Deck = Deck()
        # Declaration of the Player variable in the class
        self.Player = Player()
        # Declaration of the Dealer variable in the class
        self.Dealer = Dealer()
        # list to track card type
        self.CardType = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    # Function to draw the first 2 cards for both the dealer and the player
    def StartingCards(self):
        for x in range(2):
            draw = self.Deck.draw()
            self.Player.addCard(self.CardType[draw], draw)

        draw = self.Deck.draw()
        self.Dealer.addCard(self.CardType[draw], draw)

    def CheckDeck(self):
        if self.Deck.totalCards() < 15:
            self.Deck.reshuffle()

    #game function that brings everything together
    def PlayGame(self):
        # Variable to keep player in the game loop
        play = True

        while play:
            # Check if Deck needs to be reshuffled
            self.CheckDeck()
            # Call function to start off with 2 cards
            self.StartingCards()

            # Print the hands of the dealer and the player
            self.Player.printHand()
            self.Dealer.printHand()

            # Variable to keep track of the player's turn
            playerTurn = True
            # Variable to keep track of whether or not the player busted
            playerValid = True
            while playerTurn:
                # Check player input for hit or stand
                hitCheck = input("Would you like to hit or stand? ")
                if hitCheck == "stand":
                    playerTurn = False
                elif hitCheck == "hit":
                    draw = self.Deck.draw()
                    self.Player.addCard(self.CardType[draw], draw)
                    self.Player.printHand()
                    # Check if player busted
                    if self.Player.checkBust():
                        self.Player.printHand()
                        print("You have busted and lost")
                        playerValid = False
                        playerTurn = False
                else:
                    print("Please input a valid command")

            # Variable to keep track of Dealer's turn
            dealerTurn = True
            # Variable to keep track if the dealer busted
            dealerValid = True
            # If the player didn't bust then continue the dealer's turn
            if playerValid:
                while dealerTurn:
                    # Check if dealer wants to hit
                    if self.Dealer.hitOrStand():
                        draw = self.Deck.draw()
                        self.Dealer.addCard(self.CardType[draw], draw)
                        self.Dealer.printHand()
                        # Check if Dealer Busted
                        if self.Dealer.checkBust():
                            self.Dealer.printHand()
                            print("The Dealer has busted. You have Won")
                            dealerValid = False
                            dealerTurn = False
                    else:
                        dealerTurn = False

            # If Dealer and Player haven't busted than check to see who won
            if playerValid and dealerValid:
                self.Dealer.printHand()
                self.Player.printHand()
                if self.Player.getValue() > self.Dealer.getValue():
                    print("You have won!")
                elif self.Player.getValue() == self.Dealer.getValue():
                    print("You tied!")
                else:
                    print("you have lost...")

            # Reset both the player and dealer hand
            self.Player.resetHand()
            self.Dealer.resetHand()

            # Confirmation loop to see if player wants to keep playing
            loop = True
            while loop:
                playAgainCheck = input("Would you like to play again (Y/N): ")
                if playAgainCheck == "Y":
                    loop = False
                elif playAgainCheck == "N":
                    loop = False
                    play = False
                else:
                    print("Please input a valid command")


