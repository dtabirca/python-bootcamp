'''
Blackjack Game
Game Class File
@author https://github.com/dtabirca
@date 25.02.2020
@version 1.0
'''
from classes.deck import Deck
from classes.player import Player
from classes.dealer import Dealer

class Game:
    '''game class'''
    # pylint: disable=too-many-instance-attributes

    bust = False
    bj_pays = 3/2
    bj_player = False
    bj_dealer = False
    total_p = 0
    total_d = 0

    def __init__(self):
        '''
        game init
        '''
        #print(Deck())
        print('BlackJack pays {}'.format(self.bj_pays))
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.deck.shuffle()

    def deal_two_foreach(self):
        '''
        deal 2 cards for each player
        '''
        #one for the player
        card = self.deck.deal()
        self.player.hit(card)
        #one for the dealer, hidden
        card = self.deck.deal(message=False)
        card.hide()# one card of the dealer is hidden
        self.dealer.hit(card)
        #one for the player
        card = self.deck.deal(message=False)
        self.player.hit(card)
        #one for the dealer
        card = self.deck.deal(message=False)
        self.dealer.hit(card)
        #show table
        self.deck.draw_table(self.player.cards, self.dealer.cards)

    def check_hand(self, cards):
        '''
        counts the number of aces
        calculates hand total
        checks if busted
        @param cards
        @return total
        '''
        total = 0
        has_ace = 0
        for card in cards:
            #count aces
            if card.value == 11:
                has_ace += 1
            total += card.value
        #if total exceds 21, set aces value to 1 until total gets to 21 or below
        while total > 21 and has_ace > 0:
            total = total - 10
            has_ace -= 1
        #busted
        if total > 21:
            self.bust = True
        return total

    def players_run(self):
        '''
        hit or stand actions for the player
        '''
        while self.bj_player is False:

            self.total_p = self.check_hand(self.player.cards)
            #check hand
            if self.total_p == 21:
                #player has 21
                break
            elif self.bust:
                #bust
                print('You lost.')
                self.play_again()
                return
            else:
                while True:
                    try:
                        action = int(input('Press 1 for Hit or 2 for Stand: '))
                        break
                    except ValueError:
                        pass
                if action == 1:
                    #one for the player
                    card = self.deck.deal()
                    self.player.hit(card)
                    #show table
                    self.deck.draw_table(self.player.cards, self.dealer.cards)
                else:
                    #stand
                    self.player.stand()
                    break

    def dealers_run(self):
        '''
        hit or stand actions for the dealer
        '''
        #show hidden card
        self.dealer.cards[0].show()
        self.deck.draw_table(self.player.cards, self.dealer.cards)
        while self.bj_dealer is False and self.bj_player is False:
            # if the player has blackjack and the dealer is not,
            # dealing more cards doesn't make sense
            self.total_d = self.check_hand(self.dealer.cards)
            #check hand
            if self.total_d == 21:
                #dealer has 21
                break
            elif self.bust is True:
                #bust
                print('You won {} chip(s).'.format(2*self.player.bet_value))
                self.player.chips += 2*self.player.bet_value
                self.play_again()
                return
            elif self.total_d <= self.dealer.draw_until:
                card = self.deck.deal()
                self.dealer.hit(card)
                self.deck.draw_table(self.player.cards, self.dealer.cards)
            elif self.total_d >= self.dealer.must_stand:
                self.dealer.stand()
                break

    def conclude(self):
        '''
        decide who the winner is
        '''
        if (self.bj_player == True and self.bj_dealer == True) or (self.total_p == self.total_d):
            # tie
            print('Tie game')
            self.player.chips += self.player.bet_value
        elif self.bj_player:
            print('You won {} chip(s)'.format((self.bj_pays+1)*self.player.bet_value))
            self.player.chips += (self.bj_pays+1)*self.player.bet_value
        elif self.total_p > self.total_d:
            print('You won {} chip(s)'.format(2*self.player.bet_value))
            self.player.chips += 2*self.player.bet_value
        else:
            print('You lost.')
        self.play_again()

    def play(self):
        '''
        game thread
        '''
        #check if player has chips
        if self.player.chips == 0:
            print('You don\'t have any chips')
            quit()
        #check if enough cards
        if len(self.deck.cards) < self.deck.min_in_shoe:
            print('Not enough cards')
            self.deck.reset()
        # place bet
        print('You have {} chips'.format(self.player.chips))
        self.player.bet()
        #deal cards
        self.deal_two_foreach()
        # check player for blackjack
        self.total_p = self.check_hand(self.player.cards)
        self.bj_player = (self.total_p == 21)
        # check dealer for blackjack
        self.total_d = self.check_hand(self.dealer.cards)
        self.bj_dealer = (self.total_d == 21)
        #player first
        self.players_run()
        #dealer second
        self.dealers_run()
        #decide who the winner is
        self.conclude()

    def play_again(self):
        '''
        new game
        '''
        while True:
            action = str(input('Play again? (y/n)'))
            if action.lower() == 'y':
                self.reset()
                self.play()
                break
            elif action.lower() == 'n':
                quit()

    def reset(self):
        '''
        reset game
        '''
        self.player.cards = []
        self.dealer.cards = []
        self.player.bet_value = 1
        self.bust = False
        self.bj_player = False
        self.bj_dealer = False
        self.total_p = 0
        self.total_d = 0
        