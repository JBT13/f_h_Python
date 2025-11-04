from card import Card

class Deck:
    def __init__(self):
        suits = ["H", "S", "D", "C"]
        self.deck = []

        for suit in suits:
            for rank in range(2,15):
                new_card = Card(rank, suit)
                self.deck.append(new_card)

    def __str__(self):
        deck_str = ""
        for i, card in enumerate(self.deck):
            deck_str += str(card) + " "

            if (i + 1) % 13 == 0:
                deck_str += "\n"

        return deck_str.strip()

