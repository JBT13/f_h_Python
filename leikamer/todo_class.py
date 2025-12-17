class ToDoItem:
    def __init__(self, title, done = False):
        self.title = title 
        self.done = done
    
    def __str__(self):
        return f"Done: {self.done}"
    
class ToDoList:
    def __init__(self, items = []):
        self.items = items

    def add_item(self, title): 
        self.items.append(ToDoItem(title))

    def mark_done(self, title):
        self.title = title
        flag = False
        for item in self.items:
            if item.title == title:
                item.done = True
                flag = True

        if not flag :
            return None
        
    def __str__(self):
        all_items = ""
        for items in self.items:
            all_items += items + "\n"

        return all_items.strip()
    
# Create two distinct ToDoList objects
list_a = ToDoList()
list_b = ToDoList()

list_a.add_item("Buy Milk")
list_a.add_item("Walk Dog")

list_b.add_item("Pay Bills")

# Mark an item as done
list_a.mark_done("Buy Milk")

print("--- List A ---")
print(list_a)

print("\n--- List B (Shows the fix for mutable default args) ---")
print(list_b)