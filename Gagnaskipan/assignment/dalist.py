from fixarray import FixedSizeArray
import collections
from collections.abc import Iterable

### MADE BY SINDRI AND JEREMIAS you already know

class DAList:
    """
         Dynamic array (mimicking most of Python's list behavior).
    """

    ##############################################################################################################
    # Part 1 section
    ##############################################################################################################

    def __init__(self, capacity: int = 4):
        """
        Constructor
        Time complexity:O(n) due to FixedSizeArray
        :param capacity:
        """
        self.capacity = capacity
        self.size = 0
        self.data = FixedSizeArray(self.capacity)

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(1)
        :return: number of elements
        """
        return self.size 

    def __getitem__(self, index: int) -> object: 
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        all_index = self.wrap_index(index)
        return self.data[all_index]
    

    def __setitem__(self, index: int ,value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(1)
        :param index:
        """
        all_index = self.wrap_index(index)
        self.data[all_index] = value

    def __str__(self) -> str:
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n) n = size
        :return: string representation
        """
        string = ""
        for i in range(self.size):
            string += str(self.data[i]) + ", "
        
        return "[" + string[:-2] + "]"        


    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(n)
        :param index
        """
        all_index = self.wrap_index(index)

        for i in range(all_index, self.size-1):
            self.data[i] = self.data[i+1]

        self.data[self.size - 1] = None 
        self.size -= 1 


    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return self
        """
        self._index = 0
        return self

    def __next__(self) -> object:
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return the element at index self.__index (exception if out of range)
        """
        if self._index >= self.size:
            raise StopIteration
        
        elem: object = self.data[self._index]
        self._index += 1
        return elem
    
    def wrap_index(self, index: int) -> int:
        """
        Helper function for - and + index
        Raises Index error if out of range
        Time complexity O(1)
        :return positive index
        """
        if not -self.size <= index < self.size :
            raise IndexError("Index out of range")

        all_index = (self.size + index) % self.size
        return all_index

    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(n) due to fixed array
        """
        self.data = FixedSizeArray(self.capacity)
        self.size = 0

    def count(self, value: object) -> int:
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n)
        :return: number of times value appears
        """
        count = 0
        for i in range(self.size):
            if self.data[i] == value:
                count += 1

        return count

    def index(self, value: object) -> int:
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n)
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        for i in range(self.size):
            elem = self.data[i]
            if elem == value:
                return i
            
        raise ValueError(f"{value} is not in list")
    
    def resize(self, n):
        """
        Function that multiplies the capacity of the array by N and
        and copies all the elements of the old array to a resized array 
        Time Complexity: O(n)
        """
        new_array = FixedSizeArray(self.capacity * n)
        self.capacity *= n

        for i in range(self.size):
            new_array[i] = self.data[i]
            
        self.data = new_array


    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n)
        :param index: position where to append the element.
        :param value: element to append
        """
        if self.size >= self.capacity:
            self.resize(2)

        self.wrap_index(index)

        elem_new = value
        for i in range(index, self.size+1):
            elem_old = self.data[i]
            self.data[i] = elem_new
            elem_new = elem_old

        self.size += 1

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n)
        """
        front = 0
        for i in range(self.size-1,self.size//2,-1):
            temp = self.data[front]
            self.data[front] = self.data[i]
            self.data[i] = temp
            front += 1


    ##############################################################################################################
    # Part 2 section
    ##############################################################################################################

    def append(self, value: object):
        """
        Appends the element 'value' to the end of the array. Doubles the capacity of the array
        if it is already full before inserting an element.
        Time complexity: 0(1) if Resize: O(n)
        :param value: element to append
        """
        if self.size >= self.capacity:
            self.resize(2) 
            
        index = self.size 
        self.data[index] = value
        self.size += 1

    def copy(self) -> "DAList":
        """
        Returns a shallow copy of the array.
        Time complexity: O(n)
        :return: copy of array
        """
        ls_copy = DAList(self.capacity)
        for i in range(self.size):
            ls_copy.append(self.data[i])

        return ls_copy

    def extend(self, iterable: collections.abc.Iterable):
        """
        Extends the array with the elements from iterable.
        Time complexity: O(n)
        :param iterable: An iterable object (e.g., a list)
        """
        for i in iterable:
            self.append(i)

    def pop(self, index: int) -> object:
        """
        Remove the element at a given index from the array
        Time complexity: O(n)
        :param index: position of element to remove
        """
        all_index = self.wrap_index(index)
        value = self.data[all_index] 

        for i in range(all_index, self.size-1):
            self.data[i] = self.data[i+1]
        self.size -= 1

        return value

    def remove(self, value: object):
        """
        Removes the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n)
        :param value: The value to remove
        """
        value_index = self.index(value)      
        
        for i in range(value_index, self.size-1):
            self.data[i] = self.data[i+1]
        self.size -= 1



