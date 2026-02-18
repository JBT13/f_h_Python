from fixarray import FixedSizeArray
import collections
from collections.abc import Iterable

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
        Time complexity: ?
        :param capacity:
        """
        self.capacity = capacity
        self.size = 0
        self.array = FixedSizeArray(capacity)

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(1)
        :return: number of elements
        """
        
        return self.size

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index + self.size < 0:
            raise IndexError("Index error out of range")
        if index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index: int ,value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(1)
        :param index:
        """
        if index + self.size < 0:
            raise IndexError("Index error out of range")
        if index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __str__(self):
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n)
        :return: string representation
        """
        arr_str = ""
        brack1 = "["
        brack2 = "]"
        arr_str2 = ""
        for i in range(self.size):
            arr_str += str(self.array[i])
        
        for j in range(self.size): 
            if j == 0:
                arr_str2 += arr_str[j]
            else:
                arr_str2 += f", {arr_str[j]}"
        
        arr_str2 = brack1 + arr_str2 + brack2
        
        return arr_str2
    
    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(1)
        :param index
        """
        if index + self.size < 0:
            raise IndexError("Index error out of range")
        if index >= self.size:
            raise IndexError("Index out of range")
        
        for j in range(index, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.array[self.size - 1] = None
        

        
        

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: ?
        :return self
        """
        self.__index = 0
        return self
        

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: ?
        :return the element at index self.__index (exception if out of range)
        """
        if self.__index >= self.size:
            raise StopIteration
        elem = self.array[self.__index]
        self.__index += 1
        return elem

    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(n)
        """

        for i in range(self.size):
            del self[i]
        self.size -= self.size

    def count(self, value: object):
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n)
        :return: number of times value appears
        """
        count = 0
        for i in self.array:
            if i == value:
                count += 1
        return count

    def index(self, value: object):
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n)
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        for i in range(self.size):
            if self.array[i] == value:
                return i

        raise ValueError(f"{value} is not in list")

    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n)
        :param index: position where to append the element.
        :param value: element to append
        """
        if index > self.capacity:
            raise IndexError("Index out of range")
        
        if self.size == self.capacity:
            self.resize_array(2 * self.capacity)
        
        if index < 0:
            for j in range(-self.size, index, -1):
                self.array[j] = self.array[j + 1]

        else:
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1
        

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n)
        """
        temp_array = FixedSizeArray(self.capacity)
        for i in range(self.size):
            temp_array[i] = self.array[i]
        for j in range(self.size):
            self.array[j] = temp_array[self.size - 1 - j]

    
    def resize_array(self, cap):
        """
        Doubles the capacity of the array if it needs more space.
        Time complexity:
        """
        self.capacity = cap
        new_array = FixedSizeArray(self.capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        


    ##############################################################################################################
    # Part 2 section
    ##############################################################################################################

    def append(self, value: object):
        """
        Appends the element 'value' to the end of the array. Doubles the capacity of the array
        if it is already full before inserting an element.
        Time complexity: O(1)
        :param value: element to append
        """
        if self.size == self.capacity:
            self.resize_array(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def copy(self):
        """
        Returns a shallow copy of the array.
        Time complexity: ?
        :return: copy of array
        """
        copy_array = self
        for i in range(self.size):
            copy_array[i] = self.array[i]
        return copy_array

    def extend(self, iterable: collections.abc.Iterable):
        """
        Extends the array with the elements from iterable.
        Time complexity: O(1)
        :param iterable: An iterable object (e.g., a list)
        """
        for elem in iterable:
            self.append(elem)

    def pop(self, index: int):
        """
        Remove the element at a given index from the array
        Time complexity: ?
        :param index: position of element to remove
        """
        for i in range(self.size):
            if i == index:
                del self[i]
        self.size -= 1

    def remove(self, value: object):
        """
        Removes the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n^2)
        :param value: The value to remove
        """
        for i in range(self.size):
            if self.array[i] == value:
                del self[i]
                self.size -= 1
                return
        raise ValueError(f"{value} is not in list")
    

n = DAList()
n.append(1)
print(n)
print(n[-1])

