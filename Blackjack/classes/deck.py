'''
Blackjack Game
Deck Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
from random import shuffle
from classes.card import Card

class Deck:
    '''deck class'''

    cards = []
    min_in_shoe = 10

    def __init__(self, pack=52):
        '''
        deck init
        @param int pack
        '''
        if pack == 52:
            ranks = [['Ace', 11, 'A'], ['Two', 2, '2'], ['Three', 3, '3'],
                     ['Four', 4, '4'], ['Five', 5, '5'], ['Six', 6, '6'],
                     ['Seven', 7, '7'], ['Eight', 8, '8'], ['Nine', 9, '9'],
                     ['Ten', 10, '10'], ['Jack', 10, 'J'], ['Queen', 10, 'Q'], ['King', 10, 'K']]
            suits = [['Clubs', '♠'], ['Diamonds', '♦'], ['Hearts', '♥'], ['Spades', '♣']]
            for rank in ranks:
                for suit in suits:
                    self.cards.append(Card(rank, suit))

    def __str__(self):
        '''
        cards in deck
        @return str
        '''
        display = []
        for card in self.cards:
            display.append(card.__str__())
        return ','.join(display)

    def __len__(self):
        '''
        no of cards in deck
        '''
        return len(self.cards)

    def shuffle(self):
        '''
        shuffle deck
        '''
        print('Shuffling deck...')
        shuffle(self.cards)

    def reset(self):
        '''
        reset deck
        '''
        self.__init__()
        self.shuffle()

    def deal(self, message=True):
        '''
        deal card from deck
        @param bool (show/hide message)
        '''
        try:
            if message:
                print('Dealing cards...')
            return self.cards.pop()
        except IndexError:
            print('No more cards.')
        return False

    def draw_table(self, player_cards, dealer_cards):
        '''
        draw the table in console
        @param player_cards list
        @param dealer_cards list
        '''
        print('Player:' + 50*' ' + 'Dealer:')
        #player cards number
        pcn = len(player_cards)
        dcn = len(dealer_cards)
        space = 57 - pcn*6
        #top
        print('_'*pcn*6, end='')
        print(space*' ', end='')
        print('_'*dcn*6)
        #rank sign
        for card in player_cards:
            print('|{}'.format(card.sign)+(5-len(card.sign))*' ', end='')
        print(space*' ', end='')
        for card in dealer_cards:
            if card.hidden is False:
                print('|{}'.format(card.sign)+(5-len(card.sign))*' ', end='')
            else:
                print('|#####', end='')
        print('')
        #ascii suit
        for card in player_cards:
            print('|  {}  '.format(card.ascii), end='')
        print(space*' ', end='')
        for card in dealer_cards:
            if card.hidden is False:
                print('|  {}  '.format(card.ascii), end='')
            else:
                print('|#####', end='')
        print('')
        print('')