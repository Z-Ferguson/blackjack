from interface import Interface
from player import *
from card_deck import *

class Game:

    def __init__(self):
        self.user = Player()
        self.dealer = Dealer()
        self.interface = Interface()

    def start_game(self):
        welcome = self.interface.welcome()
        if str(welcome) == "quit":
            return False
        elif welcome:
            return self.game_loop()
        else:
            return False

    def game_loop(self):
        """Initialize the Shoe and begin the loop:
            -Deal Cards
            -Check for blackjacks
            -Allow user to hit/stand
            -Perform hits/stands for dealer
            -Determine winner
            -Prompt player for another game"""
        shoe_size = self.interface.print_options()
        if shoe_size == "quit":
            self.interface.farewell(self.user)
            return False
        self.shoe = Shoe(shoe_size)
        self.shoe.shuffle()
        while True:
            # If shoe gets down to last 20-25 cards, re-shuffle
            if len(self.shoe.cards) < 26:
                self.shoe = Shoe(shoe_size)
                self.shoe.shuffle()
            bet = self.interface.get_bet(self.user.cash)
            if bet == "quit":
                self.interface.farewell(self.user)
                return False
            self.deal_cards()
            self.interface.display_hands(self.user, self.dealer)
            self.user.is_blackjack()
            self.dealer.is_blackjack()
            while not self.user.is_blackjack():
                hit = self.player_hit_or_stand()
                if str(hit) == "quit":
                    self.interface.farewell(self.user)
                    return False
                    self.user.get_card(self.shoe.give_card())
                    self.interface.display_hands(self.user, self.dealer)
                elif hit:
                    self.user.get_card(self.shoe.give_card())
                    self.interface.display_hands(self.user, self.dealer)
                else:
                    break
            while (not self.user.busted()
                    and not self.dealer.busted()
                    and self.dealer.hit_or_stand()):
                self.dealer.get_card(self.shoe.give_card())
                self.interface.dealer_hits(self.dealer, self.user)
            else:
                self.interface.dealer_stands(self.dealer, self.user)
            self.win_or_lost(bet)
            # If player is out of money or decides to quit, end the game.
            play_again = self.interface.play_again()
            if str(play_again) == "quit":
                self.interface.farewell(self.user)
                return False
            if not play_again or self.user.cash < 1:
                self.interface.farewell(self.user)
                return False

    def win_or_lost(self, bet):
        """ Print the final state of each hand
        Check for win, loss or push in order of importance.
        1. If user busted  2. If player busted  3. If player's hand is best
        4. If tie on 21, blackjack wins else push 5. push   """
        self.interface.final_cards(self.user, self.dealer)
        if self.user.busted():
            return self.player_loses(self.user, bet)
        if self.dealer.busted():
            return self.player_wins(self.user, bet)
        if self.user.assess_hand() > self.dealer.assess_hand():
            return self.player_wins(self.user, bet)
        elif self.user.assess_hand() < self.dealer.assess_hand():
            return self.player_loses(self.user, bet)
        elif self.user.assess_hand() == 21:
            if self.user.is_blackjack() and not self.dealer.is_blackjack():
                return self.player_wins(self.user, bet)
            elif self.dealer.is_blackjack() and not self.user.is_blackjack():
                return self.player_loses(self.user, bet)
            else:
                return self.player_ties(self.user)
        else:
            return self.player_ties(self.user)

    #Deduct cash and print.
    def player_loses(self, player, bet):
        self.user.cash -= bet
        self.interface.player_loses(self.user)

    #Reward cash and print.
    def player_wins(self, player, bet):
        self.user.cash += bet
        self.interface.player_wins(self.user)

    def player_ties(self, player):
        self.interface.player_ties(self.user)

    #Give both user and dealer a new hand of cards.
    def deal_cards(self):
        self.user.get_hand(self.shoe.deal_hand())
        self.dealer.get_hand(self.shoe.deal_hand())

    #Show user and dealer's hands. Dealer hides one card.
    def show_cards(self):
        self.interface.display_hands(self.user, self.dealer)

    #Prompts player to hit or stand.
    def player_hit_or_stand(self):
        return self.interface.hit_or_stand()

    #Prints dealer's decision to hit or stand.
    def dealer_hit_or_stand(self):
        return self.interface.dealer_hit_or_stand()
