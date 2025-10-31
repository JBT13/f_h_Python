class Card:
    def __init__(self, rank, suit):
        self.suit = suit 
        
        if type(rank) is int:
            self.rank = rank

        elif type(rank) is str:
            if rank == "11":
                rank = "J"
            
            elif rank == "12":
                rank = "Q"

            elif rank == "13":
                rank = "K"
            
            elif rank == "14":
                rank = "A"
            
            else: 
                self.rank = int(rank)

                    
    def __str__(self):
        return f" {self.rank}{self.suit}"
    

# class Card:
#     def __init__(self, rank: int, suit):
#         self.suit = suit 

#         if type(rank) is int:
#             self.rank = rank
        
#         elif type(rank) is str:
#             self.rank = rank
            
#     def __str__(self):
#         return f" {self.rank}{self.suit}"