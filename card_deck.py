import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']

    def __init__(self, num):
        self.suit = Card.suits[num%4]
        self.rank = Card.rank[num//4]

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def get_next_card(self):
        if self.current_position >= len(self.cards):
            return None
        out = self.cards[self.current_position]
        self.current_position += 1
        return out

    def __repr__(self):
        return "{} of {} ".format(self.rank, self.suit)


class Deck:

    def get_next_card(self):
        out = self.cards[self.current_position]
        self.current_position += 1
        return out

    def __init__(self):
        self.cards = []
        for i in range(52):
            self.cards.append(Card(i))


    def __repr__(self):
        return "".join(repr(self.cards))


    def __getitem__(self, index):
        return self.cards[index]


class Shoe:

    def __init__(self, number_of_decks=1):
        decks = [Deck() for n in range(number_of_decks)]
        self.cards = [card for deck in decks for card in deck.cards]

    #Uses random.shuffle to shuffle the list.
    def shuffle(self):
        random.shuffle(self.cards)

    # Pops two cards from the list and returns a list containing those two card objects.
    def deal_hand(self):
        hand = [self.cards.pop(), self.cards.pop()]
        return hand

    # If cards are available, return a single card popped from the list.
    def give_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return 0

    #Returns a string version of the list of cards.
    def __str__(self):
        return str(self.cards)
