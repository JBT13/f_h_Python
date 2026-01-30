from fixarray import FixedSizeArray
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
        self.data = FixedSizeArray(self.capacity)

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: 0(1)
        :return: number of elements
        """
        # count the number of elements in the array and return the result
        return self.size

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        # return the element
        if 0 > index or index > self.size:
            raise IndexError("Index out of range")
        
        return self.data[index]

    def __setitem__(self, index: int, value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(1)
        :param index:
        """
        # set the element at the correct index to the value
        if 0 <= index <= self.capacity:
            raise IndexError("Index out of range")

        self.data[index] = value

    def __str__(self):
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n), n = size
        :return: string representation
        """
        # create a comma separated string of all the elements
        if self.size == 0:
            return "[]"
        
        ret = ",".join([str(self.data[n]) for n in range(self.size)])

        return f"[{ret}]"

    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(n), n = size
        :param index
        """
        # clear the element at the index
        for i in range(index, self.size-1):
            self.data[i] = self.data[i+1]

        self.data[self.size - 1] = None 
        self.size -= 1 

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return self
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return the element at index self.__index (exception if out of range)
        """
        # return the element at index self.index
        if self.__index >= self.size:
            raise StopIteration
        
        elem = self.data[self.__index]
        self.__index += 1
        return elem 

    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(n) n = capacity
        """
        # clear each element in the array
        self.data = FixedSizeArray(self.capacity)
        self.size = 0

    def count(self, value: object):
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n)
        :return: number of times value appears
        """
        # count the number of 
        counted = 0
        for i in range(self.size):
            if self.data[i] == value:
                counted += 1

        return counted

    def index(self, value: object):
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n) n = size 
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        # compare each element of the array to the value, if they are the same then
        # return the element's index
        for i in range(self.size):
            elem = self.data[i]
            if elem == value:
                return i
            
        raise ValueError(f"{value} is not in list")

    def resize(self, n):
        """
        O(n)
        """
        new_array = FixedSizeArray(self.capacity * n)
        self.capacity *= n

        for i in range(self.size):
            new_array[i] = self.data[i]
            
        self.data = new_array
        

    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n) n = capacity og size
        :param index: position where to append the element.
        :param value: element to append
        """
        # first check if we need to resize the array. If so, resize it
        if self.size >= self.capacity:
            self.resize(2)
        
        # insert the value, and then shift all other elements in the array to the right 
        # by one to make room for it
        elem_new = value
        for i in range(index, self.size+1):
            elem_old = self.data[i]
            self.data[i] = elem_new
            elem_new = elem_old

        # self.data[self.size] = elem_new
        self.size += 1

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n) n = size // 2
        """
        # swap each pair of elements about the center index, i.e:
        # 
        #        |               v-----|-----v            v--|--v
        # [1, 2, 3, 4, 5]  -->  [5, 2, 3, 4, 1]  -->  [5, 4, 3, 2, 1]  --> done!
        
        front = 0
        for i in range(self.size-1,self.size//2,-1):
            print(i)
            temp = self.data[front]
            self.data[front] = self.data[i]
            self.data[i] = temp
            front += 1




def HELLOWORLD(n):
    print(n)

HELLOWORLD("print")

n = DAList()

n.insert(0,1)
n.insert(0,2)
n.insert(0,3)
n.insert(0,4)
n.insert(0,5)
print(n)
