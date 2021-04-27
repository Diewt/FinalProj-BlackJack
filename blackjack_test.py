# Project: blackjack_test
# Author: Chris Diewtragulchai

import unittest
from dealer import Dealer
from player import Player
from deck import Deck


# Testing the functions from the deck class
class TestDeck(unittest.TestCase):
    # Test if the draw function is returning an index and not a null
    def test_draw_returns_value(self):
        deck = Deck()
        test = deck.draw()

        self.assertIsNotNone(test)

    # Test if the element of the card count list actually gets decremented by the function call
    def test_draw_decrements_cardCount(self):
        deck = Deck()
        deck.draw()
        test = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.assertEqual(test, deck.CardCount)

    # Test if function returns a value and not null
    def test_total_cards_returns_value(self):
        deck = Deck()
        test = deck.totalCards()

        self.assertEqual(52, test)

    # Test if function returns the correct value after drawing
    def test_total_cards_returns_correct_value(self):
        deck = Deck()
        deck.draw()
        test = deck.totalCards()

        self.assertEqual(51, test)

    # Test if reshuffling resets the deck total
    def test_reshuffle_after_draw(self):
        deck = Deck()
        deck.draw()
        deck.reshuffle()
        test = deck.totalCards()

        self.assertEqual(52, test)

    # Test if list is reset by reshuffle after a draw
    def test_reshuffle_for_list_reset(self):
        deck = Deck()
        deck.draw()
        deck.reshuffle()
        test = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        self.assertEqual(test, deck.CardCount)


# Testing the functions from the Player class
class TestPlayer(unittest.TestCase):
    def test_empty_hand(self):
        player = Player()

        self.assertEqual([], player.Hand)

    def test_adding_card(self):
        player = Player()
        player.addCard("2", 1)

        self.assertEqual(["2"], player.Hand)

    def test_adding_multiple_cards(self):
        player = Player()
        player.addCard("2", 1)
        player.addCard("King", 12)

        self.assertEqual(["2", "King"], player.Hand)

    def test_adding_card_trips_Ace_bool(self):
        player = Player()
        player.addCard("Ace", 0)

        self.assertTrue(player.Ace)

    def test_adding_card_increments_Ace_count(self):
        player = Player()
        player.addCard("Ace", 0)
        player.addCard("Ace", 0)

        self.assertEqual(2, player.AceAmount)

    def test_adding_card_affect_value1(self):
        player = Player()
        player.addCard("King", 12)

        self.assertEqual(10, player.Value)

    def test_adding_card_affect_value2(self):
        player = Player()
        player.addCard("2", 1)

        self.assertEqual(2, player.Value)

    def test_adding_card_affect_value3(self):
        player = Player()
        player.addCard("Ace", 0)

        self.assertEqual(0, player.Value)

    def test_get_value_with_simple_cards(self):
        player = Player()
        player.addCard("2", 1)
        player.addCard("3", 2)
        test = player.getValue()

        self.assertEqual(5, test)

    def test_get_value_with_face_cards(self):
        player = Player()
        player.addCard("King", 12)
        player.addCard("Queen", 11)
        test = player.getValue()

        self.assertEqual(20, test)

    def test_get_value_with_ace_as_11(self):
        player = Player()
        player.addCard("Ace", 0)
        player.addCard("2", 1)
        test = player.getValue()

        self.assertEqual(13, test)

    def test_get_value_with_ace_as_1(self):
        player = Player()
        player.addCard("Ace", 0)
        player.addCard("King", 12)
        player.addCard("King", 12)
        test = player.getValue()

        self.assertEqual(21, test)

    def test_get_value_with_multiple_aces(self):
        player = Player()
        player.addCard("Ace", 0)
        player.addCard("Ace", 0)
        test = player.getValue()

        self.assertEqual(12, test)


    def test_reset_hand_in_regard_to_hand(self):
        player = Player()
        player.addCard("Ace", 0)
        player.resetHand()

        self.assertEqual([], player.Hand)

    def test_reset_hand_in_regard_to_Ace_bool(self):
        player = Player()
        player.addCard("Ace", 0)
        player.resetHand()

        self.assertFalse(player.Ace)

    def test_reset_hand_in_regard_to_Ace_count(self):
        player = Player()
        player.addCard("Ace", 0)
        player.resetHand()

        self.assertEqual(0, player.AceAmount)

    def test_reset_hand_in_regard_to_Value(self):
        player = Player()
        player.addCard("King", 12)
        player.resetHand()

        self.assertEqual(0, player.Value)

    def test_check_bust_when_under_21(self):
        player = Player()
        player.addCard("King", 12)
        player.addCard("King", 12)

        self.assertFalse(player.checkBust())

    def test_check_bust_when_over_21(self):
        player = Player()
        player.addCard("King", 12)
        player.addCard("King", 12)
        player.addCard("King", 12)

        self.assertTrue(player.checkBust())

# Testing the Dealer Class
class TestDealer(unittest.TestCase):
    def test_empty_hand(self):
        dealer = Dealer()

        self.assertEqual([], dealer.Hand)

    def test_adding_card(self):
        dealer = Dealer()
        dealer.addCard("2", 1)

        self.assertEqual(["2"], dealer.Hand)

    def test_adding_multiple_cards(self):
        dealer = Dealer()
        dealer.addCard("2", 1)
        dealer.addCard("King", 12)

        self.assertEqual(["2", "King"], dealer.Hand)

    def test_adding_card_trips_Ace_bool(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)

        self.assertTrue(dealer.Ace)

    def test_adding_card_increments_Ace_count(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.addCard("Ace", 0)

        self.assertEqual(2, dealer.AceAmount)

    def test_adding_card_affect_value1(self):
        dealer = Dealer()
        dealer.addCard("King", 12)

        self.assertEqual(10, dealer.Value)

    def test_adding_card_affect_value2(self):
        dealer = Dealer()
        dealer.addCard("2", 1)

        self.assertEqual(2, dealer.Value)

    def test_adding_card_affect_value3(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)

        self.assertEqual(0, dealer.Value)

    def test_get_value_with_simple_cards(self):
        dealer = Dealer()
        dealer.addCard("2", 1)
        dealer.addCard("3", 2)
        test = dealer.getValue()

        self.assertEqual(5, test)

    def test_get_value_with_face_cards(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.addCard("Queen", 11)
        test = dealer.getValue()

        self.assertEqual(20, test)

    def test_get_value_with_ace_as_11(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.addCard("2", 1)
        test = dealer.getValue()

        self.assertEqual(13, test)

    def test_get_value_with_ace_as_1(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.addCard("King", 12)
        dealer.addCard("King", 12)
        test = dealer.getValue()

        self.assertEqual(21, test)

    def test_get_value_with_multiple_aces(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.addCard("Ace", 0)
        test = dealer.getValue()

        self.assertEqual(12, test)


    def test_reset_hand_in_regard_to_hand(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.resetHand()

        self.assertEqual([], dealer.Hand)

    def test_reset_hand_in_regard_to_Ace_bool(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.resetHand()

        self.assertFalse(dealer.Ace)

    def test_reset_hand_in_regard_to_Ace_count(self):
        dealer = Dealer()
        dealer.addCard("Ace", 0)
        dealer.resetHand()

        self.assertEqual(0, dealer.AceAmount)

    def test_reset_hand_in_regard_to_Value(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.resetHand()

        self.assertEqual(0, dealer.Value)

    def test_check_bust_when_under_21(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.addCard("King", 12)

        self.assertFalse(dealer.checkBust())

    def test_check_bust_when_over_21(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.addCard("King", 12)
        dealer.addCard("King", 12)

        self.assertTrue(dealer.checkBust())

    def test_hit_or_stand_for_value_less_than_17(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.addCard("2", 1)

        self.assertTrue(dealer.hitOrStand())

    def test_hit_or_stand_for_value_greater_than_17(self):
        dealer = Dealer()
        dealer.addCard("King", 12)
        dealer.addCard("Ace", 0)

        self.assertFalse(dealer.hitOrStand())


if __name__ == "__main__":
    unittest.main()
