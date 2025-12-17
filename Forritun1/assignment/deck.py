from card import Card
import random

class Deck:
    """
    Represents a normal deck of 52 playing cards
    """
    def __init__(self):
        """
        Initializes a new deck of 52 cards, ordered by suit (H, S, D, C)
        and then by rank (2-A)
        """
        suits = ["H", "S", "D", "C"]
        self.deck = []

        for suit in suits:
            for rank in range(2,15):
                new_card = Card(rank, suit)
                self.deck.append(new_card)
                # creates the 52 cards in order

    def __str__(self) -> str:
        """
        Returns the string representation of the deck, listing all cards
        with 13 cards per line
        """
        deck_str = ""
        for i, card in enumerate(self.deck):
            deck_str += str(card) + " "

            # new line every 13 cards
            if (i + 1) % 13 == 0:
                deck_str += "\n"

        return deck_str.rstrip()

    def shuffle(self):
        """
        Shuffles the cards in the deck randomly in place
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Deals a single card from the top (beginning) of the deck
        """
        return self.deck.pop(0)