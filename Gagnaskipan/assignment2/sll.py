#
# Gagnaskipan.
# Single-Linked-List
# Student(s): Jeremias Borjas Tablante, 
#             Sindri Freysson
#             (THE GOATS!!!!)
#                  :-)
from sll_node import Node
from iterator import NodeIterator

class SLList:

    def __init__(self):
        """
        Constructor.
        Time complexity: O(1)
        """
        self._tail = Node(None,None)
        self._head = Node(None,None)
        self._len = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._head)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        node = self._head
        while node:
            elems.append(str(node.item))
            node = node.next
        return '[' + ', '.join(elems) + ']'

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._len

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return self._len == 0  # could alternatively check _tail is None, or _len is 0.

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('front called on an empty list')
        return self._head.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('back called on an empty list')
        return self._tail.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        if not self._head:
            new_node = Node(item,None)
            self._head = new_node
            self._tail = new_node  

        else:
            new_node = Node(item,self._head)
            self._head = new_node
        
        self._len += 1

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self._len == 0:
            raise RuntimeError ("Empty list")

        item = self._head.item
        new_head = self._head.next
        value = self._head
        del value
        self._head = new_head
        self._len -= 1

        return item

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
          :return: None
        """
        if not self._head:
            new_node = Node(item,None)
            self._head = new_node
            self._tail = new_node 

        else:
            new_node = Node(item, None)
            self._tail.next = new_node
            self._tail = new_node
        
        self._len += 1

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(n)
        :return: None, but trows an exception if list empty.
        """
        if self._len == 0:
            raise RuntimeError ("Empty list")

        if self._len == 1:
            current_node = self._head.item
            self._head = Node(None,None)
            self._tail = Node(None,None)
            self._len -= 1

            return current_node


        current_node = self._head
        old_node_item = None
        while current_node:
            if current_node.next.next:
                current_node = current_node.next
                continue
            
            else:
                old_node = current_node.next
                old_node_item = current_node.item
                current_node.next = None
                del old_node 
                self._tail = current_node
                break
        
        self._len -= 1

        return old_node_item


def main():
    a = SLList()
    a.push_front(1)
    print(a)
    a.pop_front()
    print(a)
    a.pop_front()
    print(a)
    a.push_back(2)
    print(a)
    a.push_back(3)
    print(a)
    a.push_front(2)
    print(a)
    

if __name__ == "__main__":
    main()


