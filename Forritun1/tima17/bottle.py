class WaterBottle:
    def __init__(self, max_capacity = 2):
        self.max_capacity = max_capacity
        self.current_contents = 0

    def fill(self):
        self.current_contents = self.max_capacity
        return  
        
    def drink(self, amount: float) -> float:
        self.amount = amount
        if amount <= 0:
            return 0
        elif amount > self.current_contents:
            the_amount = self.current_contents
            self.current_contents = 0
            return the_amount 
        else:
            self.current_contents -= self.amount
            return amount
    
    def __str__(self) -> str:
        return f"The bottle currently holds {self.current_contents:.1f}L of water."
    

