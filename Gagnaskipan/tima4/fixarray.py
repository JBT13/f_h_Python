import ctypes

class DynSizeArray:

    """
        Fixed-size array (using the ctypes package to access the underlying C-code interface).
    """

    def __init__(self, capacity: int = 4):
        """
        Creates an array of a fixed size, where each element is an object reference.
        :param capacity: array's capacity/size
        """
        self.size = 0
        if capacity <= 0:
            raise ValueError("FixedSizeArray capacity must be positive")
        self.__capacity = capacity
        self.__array = (ctypes.py_object * self.__capacity)()
        for i in range(self.__capacity):
            self.__array[i] = None   # Strictly speaking, not needed (NULL/None by default)

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (x = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index < 0 or index >= self.__capacity:
            raise IndexError("Index out of range")
        return self.__array[index]
    
    def __len__(self):
        """
        O(1)
        """
        return self.size


    def __setitem__(self,index: int ,value: object):
        """
        Updating an element at given index (A[index] = x).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index < 0 or index >= self.__capacity:
            raise IndexError("Index out of range")
        self.__array[index] = value

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return:
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return the element at index self.__index (exception if out of range)
        """
        if self.__index >= self.size:
            raise StopIteration
        elem = self.__array[self.__index]
        self.__index += 1
        return elem

    def capacity(self) -> int:
        """
        Returns the capacity of the array.
        :return: array's capacity
        """
        return self.__capacity
    
    def clear_1(self):
        """
        O(n)
        """
        self.__array = (ctypes.py_object * self.capacity())()
        self.size = 0

    def __str__(self):
        """
        O(n)
        """
        if self.size == 0:
            return "[]"
        
        ret = ",".join([str(self.__array[n]) for n in range(self.size)])
        
        return f"[{ret}]"
        
    def count_value(self,value: object):
        """
        O(n)
        """
        count = 0
        for i in range(self.size):
            if self.__array[i] == value:
                count += 1
            
        return count
    
    def reverse_1(self):
        """
        O(n)
        """
        front = 0
        for i in range(self.size-1,self.size//2,-1):
            print(i)
            temp = self.__array[front]
            self.__array[front] = self.__array[i]
            self.__array[i] = temp
            front += 1

    def resize(self):
        """
        O(n)
        """
        new_array = (ctypes.py_object * self.__capacity)()

        for i in range(self.size):
            new_array[i] = self.__array[i]
            
        self.__array = new_array

    def append_1(self, value: object):
        """
        O(1)
        """
        if self.size >= self.__capacity:
            self.__capacity *= 2
            self.resize()
            

        index = self.__len__() 
        self.__array[index] = value
        self.size += 1

    def pop_1(self):
        """
        O(n)
        """
        if self.size == 0:
            raise IndexError("Cannot pop my goat")
        
        value = self.__array[self.size - 1]
        self.__array[self.size -1] = None
        self.size -= 1

        return value