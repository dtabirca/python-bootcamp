'''
Blackjack Game
Card Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
class Card:
    '''card class'''

    def __init__(self, rank, suit):
        '''
        card init
        @param rank, suit
        '''
        self.rank = rank[0]
        self.value = rank[1]
        self.sign = rank[2]
        self.suit = suit[0]
        self.ascii = suit[1]
        self.hidden = False

    def __str__(self):
        '''
        rank and suit of the card
        @return str
        '''
        return self.rank + ' of ' + self.suit

    def hide(self):
        '''
        hidden card
        '''
        self.hidden = True

    def show(self):
        '''
        visible card
        '''
        self.hidden = False

    def draw_front(self):
        '''
        card's front side
        '''
        print('______')
        print('|{}    '.format(self.sign))
        print('|  {}  '.format(self.ascii))
        print('|      ')

    @classmethod
    def draw_back(cls):
        '''
        card's back side
        '''
        print('______')
        print('|#####')
        print('|#####')
        print('|#####')
        