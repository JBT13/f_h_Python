class Pokemon:
  def __init__(self, entry: int, name: str, types: list, description: str, is_caught: bool):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught  
  
  def speak(self):
    print(self.name * 2)
  
  def display_details(self):
    print(f"Entry Number: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Type: {self.types}")
    print(f"Description: {self.description}")

