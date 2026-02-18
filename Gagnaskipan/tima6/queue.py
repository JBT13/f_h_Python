import ctypes

class Queue:
    def __init__(self, capacity: int = 4):
        self.size = 0
        self.top = 0
        self.capacity = capacity
        self.array = (ctypes.py_object * self.capacity)()
        for i in range(self.capacity):
            self.array[i] = None 

    def enqueue(self, item: object):
        if self.size == self.capacity:
            raise IndexError("The queue is full my brother")
        
        index = (self.top + self.size) % self.capacity
        self.array[index] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty my brother")
        
        if self.size == 0:
            self.top = 0 

        index = self.top
        value = self.array[index]
        self.array[index] = None
        self.size -= 1
        self.top = (self.top + 1) % self.capacity   
        return value

    def front(self):
        value = self.array[(self.top + self.size) % self.capacity]
        return value

    def is_empty(self):
        return self.size == 0
        
    def is_full(self):
        return self.size == self.capacity 
        
    def __str__(self):
        string = ""
        for i in range(self.capacity):
            if self.array[(self.top + i) % self.capacity] is None:
                continue
            string += str(self.array[(self.top + i) % self.capacity]) + ", "
        return "[" + string[:-2] + "]"  
    
class DQueue(Queue):
    def __init__(self, capacity = 4):
        super().__init__(capacity)

    def resize(self):
        new_array = (ctypes.py_object * (self.capacity*2))()
        for i in range(self.capacity):
            new_array[i] = None 

        new_array = (ctypes.py_object * (self.capacity * 2))()

        for i in range(self.capacity):
            new_array[i] = self.array[i]

        self.capacity *= 2
        self.array = new_array

    def enqueue(self, item):
        if self.size == self.capacity:
            self.resize()
        return super().enqueue(item)
    
    def dequeue(self):
        return super().dequeue()
    
    def front(self):
        return super().front()

    def is_full(self):
        return super().is_full()
    
    def is_empty(self):
        return super().is_empty()
    
    def __str__(self):
        return super().__str__()
    


