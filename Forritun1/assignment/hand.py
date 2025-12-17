class Hand:
    """
    Represents a collection of cards held by a player, up to a maximum size
    """
    NUMBER_OF_CARDS = 13

    def __init__(self):
        """
        Initializes an empty hand
        """
        self.cards = []

    def __str__(self):
        """
        Returns a single line string of all cards in the hand
        each followed by a single space. Returns "Empty" if no cards are present
        """
        if not self.cards:
            return "Empty"
        
        card_strings = [str(card) for card in self.cards]

        return " ".join(card_strings) + " " #freaking white space

    def add_card(self, card):
        """
        Adds a Card object to the hand if the hand is not full
        """
        if len(self.cards) <  Hand.NUMBER_OF_CARDS:
            self.cards.append(card)

