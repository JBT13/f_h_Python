class Card:
    """
    A normal playing card with a rank (2-14) and a suit (H, S, D, C)
    """
    def __init__(self, rank, suit):
        """
        Initializes a Card object

        :param rank: The rank of the card, either as an integer (2-14) or a string ('A', 'K', '10', etc.)
        :param suit: The suit of the card ('H', 'S', 'D', or 'C')
        """
        self.suit = suit 
        
        if type(rank) is int:
            self.rank = rank
        elif type(rank) is str:
            # Dictionary to handle face cards and string numbers for ranks 11-14
            rank_dic = {'A': 14, 'K': 13, 'Q': 12, 'J': 11,
                        '14': 14, '13': 13, '12': 12, '11': 11}
            
            if rank.upper() in rank_dic:
                self.rank = rank_dic[rank.upper()]
            else: 
                # Handles string numbers 2-10
                self.rank = int(rank)

    def __str__(self):
        """
        Returns the string representation of the card (e.g., " AS", "10H")
        right-justified in a 3-character field
        """
        if self. rank == 14:
            rank_str = "A"
        elif self. rank == 13:
            rank_str = "K"
        elif self. rank == 12:
            rank_str = "Q"
        elif self. rank == 11:
            rank_str = "J"
        else:
            rank_str = str(self.rank)

        card_str = rank_str + self.suit
        return f"{card_str:>3}"
    
