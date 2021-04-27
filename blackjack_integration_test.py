# Project: blackjack integration test
# Author: Chris Diewtragulchai

import unittest
from blackjack import Blackjack


class TestBlackJackDeck(unittest.TestCase):
    def test_variable_element_deck1(self):
        blackjack = Blackjack()

        self.assertEqual(4, blackjack.Deck.StandardAmount)

    def test_variable_element_deck2(self):
        blackjack = Blackjack()
        test = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.assertEqual(test, blackjack.Deck.CardCount)

    def test_deck_variable_function_draw(self):
        blackjack = Blackjack()
        test = blackjack.Deck.draw()

        self.assertIsNotNone(test)

    def test_deck_variable_function_draw_decrements_cardCount(self):
        blackjack = Blackjack()
        blackjack.Deck.draw()
        test = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.assertNotEqual(test, blackjack.Deck.CardCount)

    def test_deck_variable_function_total_cards(self):
        blackjack = Blackjack()
        test = blackjack.Deck.totalCards()

        self.assertEqual(52, test)

    def test_deck_variable_function_total_cards2(self):
        blackjack = Blackjack()
        blackjack.Deck.draw()
        test = blackjack.Deck.totalCards()

        self.assertEqual(51, test)

    def test_deck_variable_function_reshuffle(self):
        blackjack = Blackjack()
        blackjack.Deck.draw()
        blackjack.Deck.reshuffle()
        test = blackjack.Deck.totalCards()

        self.assertEqual(52, test)

    def test_deck_variable_function_reshuffle2(self):
        blackjack = Blackjack()
        blackjack.Deck.draw()
        blackjack.Deck.reshuffle()
        test = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.assertEqual(test, blackjack.Deck.CardCount)


class TestBlackJackPlayer(unittest.TestCase):
    def test_player_variable(self):
        blackjack = Blackjack()

        self.assertEqual([], blackjack.Player.Hand)

    def test_player_function_add_card(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("2", 1)

        self.assertEqual(["2"], blackjack.Player.Hand)

    def test_player_function_add_card2(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("2", 1)
        blackjack.Player.addCard("King", 12)

        self.assertEqual(["2", "King"], blackjack.Player.Hand)

    def test_player_function_add_card3(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)

        self.assertTrue(blackjack.Player.Ace)

    def test_player_function_add_card4(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.addCard("Ace", 0)

        self.assertEqual(2, blackjack.Player.AceAmount)

    def test_player_function_add_card5(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("King", 12)

        self.assertEqual(10, blackjack.Player.Value)

    def test_player_function_add_card6(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("2", 1)

        self.assertEqual(2, blackjack.Player.Value)

    def test_player_function_add_card7(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)

        self.assertEqual(0, blackjack.Player.Value)

    def test_player_function_getValue(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("2", 1)
        blackjack.Player.addCard("3", 2)
        test = blackjack.Player.getValue()

        self.assertEqual(5, test)

    def test_player_function_getValue2(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("King", 12)
        blackjack.Player.addCard("Queen", 11)
        test = blackjack.Player.getValue()

        self.assertEqual(20, test)

    def test_player_function_getValue3(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.addCard("2", 1)
        test = blackjack.Player.getValue()

        self.assertEqual(13, test)

    def test_player_function_getValue4(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.addCard("King", 12)
        test = blackjack.Player.getValue()

        self.assertEqual(21, test)

    def test_player_function_getValue5(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.addCard("Ace", 0)
        test = blackjack.Player.getValue()

        self.assertEqual(12, test)

    def test_player_function_resetHand(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.resetHand()

        self.assertEqual([], blackjack.Player.Hand)

    def test_player_function_resetHand2(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.resetHand()

        self.assertFalse(blackjack.Player.Ace)

    def test_player_function_resetHand3(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("Ace", 0)
        blackjack.Player.resetHand()

        self.assertEqual(0, blackjack.Player.AceAmount)

    def test_player_function_resetHand4(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("King", 12)
        blackjack.Player.resetHand()

        self.assertEqual(0, blackjack.Player.Value)

    def test_player_function_checkBust(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("King", 12)
        blackjack.Player.addCard("King", 12)

        self.assertFalse(blackjack.Player.checkBust())

    def test_player_function_checkBust2(self):
        blackjack = Blackjack()
        blackjack.Player.addCard("King", 12)
        blackjack.Player.addCard("King", 12)
        blackjack.Player.addCard("King", 12)

        self.assertTrue(blackjack.Player.checkBust())


class TestBlackJackDealer(unittest.TestCase):
    def test_dealer_variable(self):
        blackjack = Blackjack()

        self.assertEqual([], blackjack.Dealer.Hand)

    def test_dealer_function_add_card(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("2", 1)

        self.assertEqual(["2"], blackjack.Dealer.Hand)

    def test_dealer_function_add_card2(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("2", 1)
        blackjack.Dealer.addCard("King", 12)

        self.assertEqual(["2", "King"], blackjack.Dealer.Hand)

    def test_dealer_function_add_card3(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)

        self.assertTrue(blackjack.Dealer.Ace)

    def test_dealer_function_add_card4(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.addCard("Ace", 0)

        self.assertEqual(2, blackjack.Dealer.AceAmount)

    def test_dealer_function_add_card5(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)

        self.assertEqual(10, blackjack.Dealer.Value)

    def test_dealer_function_add_card6(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("2", 1)

        self.assertEqual(2, blackjack.Dealer.Value)

    def test_dealer_function_add_card7(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)

        self.assertEqual(0, blackjack.Dealer.Value)

    def test_dealer_function_getValue(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("2", 1)
        blackjack.Dealer.addCard("3", 2)
        test = blackjack.Dealer.getValue()

        self.assertEqual(5, test)

    def test_dealer_function_getValue2(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("Queen", 11)
        test = blackjack.Dealer.getValue()

        self.assertEqual(20, test)

    def test_dealer_function_getValue3(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.addCard("2", 1)
        test = blackjack.Dealer.getValue()

        self.assertEqual(13, test)

    def test_dealer_function_getValue4(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.addCard("King", 12)
        test = blackjack.Dealer.getValue()

        self.assertEqual(21, test)

    def test_dealer_function_getValue5(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.addCard("Ace", 0)
        test = blackjack.Dealer.getValue()

        self.assertEqual(12, test)

    def test_dealer_function_resetHand(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.resetHand()

        self.assertEqual([], blackjack.Dealer.Hand)

    def test_dealer_function_resetHand2(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.resetHand()

        self.assertFalse(blackjack.Dealer.Ace)

    def test_dealer_function_resetHand3(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("Ace", 0)
        blackjack.Dealer.resetHand()

        self.assertEqual(0, blackjack.Dealer.AceAmount)

    def test_dealer_function_resetHand4(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.resetHand()

        self.assertEqual(0, blackjack.Dealer.Value)

    def test_dealer_function_checkBust(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("King", 12)

        self.assertFalse(blackjack.Dealer.checkBust())

    def test_dealer_function_checkBust2(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("King", 12)

        self.assertTrue(blackjack.Dealer.checkBust())

    def test_dealer_function_hitOrStand(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("2", 1)

        self.assertTrue(blackjack.Dealer.hitOrStand())

    def test_dealer_function_hitOrStand2(self):
        blackjack = Blackjack()
        blackjack.Dealer.addCard("King", 12)
        blackjack.Dealer.addCard("Ace", 0)

        self.assertFalse(blackjack.Dealer.hitOrStand())


if __name__ == "__main__":
    unittest.main()