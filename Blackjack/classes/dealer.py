'''
Blackjack Game
Dealer Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
class Dealer:
    '''dealer'''
    draw_until = 16
    must_stand = 17
    cards = []

    def __init__(self):
        '''
        dealer init
        '''
        print('Dealer must draw to {} and stand on {}'.format(self.draw_until, self.must_stand))

    def hit(self, card):
        '''
        @param card
        '''
        self.cards.append(card)

    def stand(self):
        '''method'''

    def bet(self):
        '''method'''
