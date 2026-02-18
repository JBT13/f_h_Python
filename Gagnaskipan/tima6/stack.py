import ctypes

class Stack:
    def __init__(self, capacity: int = 4):
        self.size = 0
        self.__capacity = capacity
        self.__array = (ctypes.py_object * self.__capacity)()
        for i in range(self.__capacity):
            self.__array[i] = None 

    def resize(self, n):
        new_array = (ctypes.py_object * self.capacity * n)()
        self.capacity *= n

        for i in range(self.size):
            new_array[i] = self.data[i]
            
        self.data = new_array

    def push(self, item: object):
        if self.size >= self.__capacity:
            self.resize(2) 
            
        index = self.size 
        self.__array[index] = item
        self.size += 1
        pass

    def pop(self):
        value = self.__array[self.size -1]
        self.__array[self.size - 1] = None
        self.size -= 1

        return value

    def top(self):
        value = self.__array[self.size - 1]
        return value

    def is_empty(self):
        return self.size == 0
        
        
    def __str__(self):
        string = ""
        for i in range(self.size):
            string += str(self.__array[i]) + ", "
        
        return "[" + string[:-2] + "]"  
    
