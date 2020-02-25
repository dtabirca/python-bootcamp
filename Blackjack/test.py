'''
Blackjack Game
UnitTest Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
import unittest
from classes.game import Game
from classes.deck import Deck

class TestGame(unittest.TestCase):
	'''class'''
	def test_deck(self):
		'''test deck'''
		deck = Deck(52)
		deck.shuffle()
		for index in range(52):
			card = deck.deal()
			print('{}. {}'.format(index+1, card.__str__()))
		no_of_cards = len(deck)
		self.assertEqual(no_of_cards, 0)

if __name__ == '__main__':
    unittest.main()
