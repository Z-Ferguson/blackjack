class Player:
    def __init__(self):
        self.cards = []
        self.cash = 100
        self.blackjack = False

    # Receives a list of Cards and stores as players cards
    def get_hand(self, new_cards):
        self.cards = new_cards

    # Adds card to player's list of cards
    def get_card(self, new_card):
        self.cards.append(new_card)

    #Returns cards for interface to display.
    def display_hand(self):
        return self.cards

    # Assesses value of hand by counting number of aces as it adds the values of all the other cards.
    # If the hand busts and there exists an Ace, use the value of 1 rather than 11
    # by deducting 10 from the hand value.
    def assess_hand(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            try:
                if 2 <= card.rank <= 10:
                    value += card.rank
            except:
                if card.rank in ["Jack", "Queen", "King"]:
                    value += 10
                elif card.rank == "Ace":
                    value += 11
                    ace_count += 1
        while ace_count > 0:
            if value > 21:
                value -= 10
            ace_count -= 1
        return value

    # Returns True if the hand has busted.
    def busted(self):
        return self.assess_hand() > 21

    # This is used to determine the winner
    def is_blackjack(self):
        if self.assess_hand() == 21:
            self.blackjack = True
        else:
            self.blackjack = False
        return self.blackjack


class Dealer(Player):
    #Initialize the dealer
    def __init__(self):
        pass

    #Dealer shows all but one cards on a typical display.
    def display_hand(self):
        return self.cards[1:]

    # Only called at the end of the game. This shows the dealer's entire hand
    def display_entire_hand(self):
        return self.cards

    # Return True to hit (get another card), else False to stand.
    # If hand is less than 17 or was dealt a soft 17, Hit
    def hit_or_stand(self):
        if self.assess_hand() < 17:
            return True
        elif (len(self.cards) == 2 and self.assess_hand() == 17 and
              (self.cards[0].rank == "Ace" or self.cards[1].rank == "Ace")):
            return True
        else:
            return False
