
from player import Player
from player import Dealer


class Interface:
    def __init__(self):
        pass

    def welcome(self):
        print("""\n\nWelcome to the game of blackjack!""")
        print("""Would you like to play a game?""")
        return self.yes_or_no()

    def print_options(self):
        print("""Would you like to choose the size of the shoe?""")
        options = self.yes_or_no()
        if str(options) == "quit":
                return "quit"
        elif options:
            return self.get_shoe_size()
        else:
            return 1

    def get_shoe_size(self):
        print("Great!\nPlease enter a size between 1 and 8.")
        return self.get_shoe_input()

    def get_bet(self, max_bet):
        if max_bet > 1:
            print("How much would you like to bet?  $1 - {}".format(max_bet))
        else:
            print("You've got one dollar left.  Make it worth it!")
            return 1
        return self.get_bet_input(max_bet)

    # Shows all player's cards and all but one dealer card.
    def display_hands(self, player, dealer):
        player_hand = player.display_hand()
        dealer_hand = dealer.display_hand()
        max_length = max(len(player_hand), len(dealer_hand))
        print("Your Hand:".ljust(30), "Dealer Hand".ljust(30))
        for n in range(0, max_length):
            try:
                print(str(player_hand[n]).ljust(30),
                      str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30), str(dealer_hand[n]).ljust(60))
        print("Your Value: {}".format(player.assess_hand()).ljust(30), "\n")
        return "{}\n{}".format(player_hand, dealer_hand)

    def player_wins(self, player):
        """ Player wins, shows current cash. """
        print("You win!", "\n")
        self.players_pot(player)

    def player_loses(self, player):
        print("You lose.", "\n")
        self.players_pot(player)

    def player_ties(self, player):
        print("Game is a tie.", "\n")
        self.players_pot(player)

    def players_pot(self, player):
        print("You currently have ${}".format(player.cash), "\n")

    def hit_or_stand(self):
        print("Another Card?")
        hit = self.yes_or_no()
        return hit

    def dealer_hits(self, dealer, player):
        print(" ".ljust(30), "Dealer hits:")
        self.display_hands(player, dealer)

    def dealer_stands(self, dealer, player):
        print(" ".ljust(30), "Dealer stands")
        self.display_hands(player, dealer)

    def play_again(self):
        print("Would you like to play again?")
        return self.yes_or_no()

    def busted(self):
        print("You've busted.")
        print("Game over.\n")

    def final_cards(self, player, dealer):
        player_hand = player.display_hand()
        dealer_hand = dealer.display_entire_hand()
        max_length = max(len(player_hand), len(dealer_hand))
        print("Your Hand:".ljust(30), "Dealer Hand".ljust(30))
        for n in range(0, max_length):
            try:
                print(str(player_hand[n]).ljust(30),
                      str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30), str(dealer_hand[n]).ljust(60))
        print(("Your Value: {}".format(player.assess_hand()).ljust(30)),
              ("Dealer Value: {}".format(dealer.assess_hand()).ljust(30)),
              "\n")
        return "{}\n{}".format(player_hand, dealer_hand)

    def farewell(self, player):
        print("Thanks for playing!")
        print("You're leaving with ${}".format(player.cash))
        if player.cash < 1:
            print("Better luck next time, champ")

    def get_bet_input(self, max_bet, try_count=1):
        if try_count > 3:
            # Defaults to $10 bets if user enters bad input.
            # However, if user doesn't have $10, make them bet everything.
            if max_bet >= 10:
                return 10
            else:
                return max_bet
        bet = input(">>")
        try:
            if 0 < int(bet) <= max_bet:
                return int(bet)
            else:
                return self.get_bet_input(max_bet, try_count+1)
        except:
            if bet == "quit":
                return "quit"
            else:
                return self.get_bet_input(max_bet, try_count+1)

    def get_shoe_input(self, try_count=1):
        if try_count > 3:
            print("You've chosen 1 deck!")
            return 1
        size = input(">>")
        try:
            if 0 < int(size) <= 8:
                if size == 1:
                    print("You've chosen 1 deck!")
                else:
                    print("You've chosen {} decks!".format(size))
                return int(size)
            else:
                return self.get_shoe_input(try_count+1)
        except:
            if size == "quit":
                return "quit"
            else:
                return self.get_shoe_input(try_count+1)

    def yes_or_no(self):
        print("[Y]es")
        print("[N]o")
        answer = input(">>").lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        elif answer == "quit":
            return "quit"
        else:
            return self.yes_or_no()
