'''
Blackjack Game
Player Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
class Player:
    '''class player'''

    chips = 100
    cards = []
    bet_value = 1

    def __init__(self):
        '''init player'''

    def __str__(self):
        '''
        no of chips
        @return str
        '''
        return 'Player has {} chips'.format(self.chips)

    def hit(self, card):
        '''
        @param card
        '''
        self.cards.append(card)

    def stand(self):
        '''method'''

    def split(self):
        '''method'''

    def double(self):
        '''method'''

    def surrender(self):
        '''method'''

    def bet(self):
        '''
        place bet
        '''
        while True:
            try:
                bet = float(input('Place your bet: '))
                if bet > self.chips:
                    print('Not enough chips!')
                else:
                    self.chips -= bet
                    self.bet_value = bet
                    print('Your bet is {} chips. {} chips remaining.'.format(bet, self.chips))
                    return
            except ValueError:
                print('Must be a number')
