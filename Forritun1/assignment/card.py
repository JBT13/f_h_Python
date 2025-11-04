class Card:
    def __init__(self, rank, suit):
        self.suit = suit 
        
        if type(rank) is int:
            self.rank = rank

        elif type(rank) is str:
            rank_dic = {'A': 14, 'K': 13, 'Q': 12, 'J': 11,
                        '14': 14, '13': 13, '12': 12, '11': 11}
            
            if rank.upper() in rank_dic:
                self.rank = rank_dic[rank.upper()]
            else: 
                self.rank = int(rank)

                    
    def __str__(self):
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

        return f" {rank_str}{self.suit}"
    
