#
# Gagnaskipan.
# Double-Linked-List
# Student(s): Jeremias Borjas Tablante, 
#             Sindri Freysson
#             (THE GOATS!!!!)
#                  :-)

from dll_node import Node
from iterator import NodeIterator

class Position:
    __slots__ = ['node']

    def __init__(self, node):
        self.node: Node = node


class DLList:

    #
    # Beginning of fundamental section.
    #

    def __init__(self):
        self._head = Node(prev="Sentinel")
        self._tail = Node(next="Sentinel")
        self._head.next = self._tail
        self._tail.prev = self._head
        self.size = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        self.iterator = NodeIterator(self._head.next)
        return self
    
    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        node: Node = self._head.next
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
        return self.size

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return self.size == 0


    def error_handler(self, pos: Position):
        if self.is_empty():
            raise RuntimeError("Empty list")

        if pos.node.next is None and pos.node.prev is None:
            raise RuntimeError("Position does not exist")


    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """
        self.error_handler(pos)

        return pos.node.item

    def append_empty_list(self,item):
        """
        Append element when list is empty
        :param item: Object
        :return Position of inserted element
        """
        new_node = Node(self._head, item, self._tail)
        self._head.next = new_node
        self._tail.prev = new_node
        self.size += 1
        pos = Position(new_node)
        pos.node = new_node

        return pos


    def insert_after(self, pos: Position, item: object) -> Position:
        """pos
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        if self.is_empty():
            return self.append_empty_list(item)

        if pos.node.item is None:
            raise RuntimeError("Position does not exist")

        inserted_node = Node(pos.node, item, pos.node.next)
        current_node = pos.node
        next_node: Node = pos.node.next
        current_node.next = inserted_node
        next_node.prev = inserted_node
        pos.node = inserted_node

        self.size += 1

        return pos 
        

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """            
        if self.is_empty():
            return self.append_empty_list(item)

        if pos.node.item is None:
            raise RuntimeError("Position does not exist")

        inserted_node = Node(pos.node.prev, item, pos.node )
        current_node = pos.node
        before_node: Node = pos.node.prev
        current_node.prev = inserted_node
        before_node.next = inserted_node
        pos.node = inserted_node

        self.size += 1

        return pos 


    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        if pos.node.next is None and pos.node.prev is None:
            raise RuntimeError("Position does not exist")

        next_node: Node = pos.node.next 
        behind_node: Node = pos.node.prev

        next_node.prev = behind_node
        behind_node.next = next_node
        self.size -= 1
        removed_element = pos.node.item
        pos.node.prev = None
        pos.node.next = None

        return removed_element 
 

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        if pos.node.item is None:
            raise RuntimeError("Position does not exist")
        
        current_item = pos.node.item
        pos.node.item = item 

        return current_item


    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return

        return Position(self._head.next)

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return
        
        return Position(self._tail.prev)

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        if pos.node.prev is None:
            return None

        return Position(pos.node.prev)


    def next_pos(self, pos: Position) -> Position | None:
        """
         Return position following 'pos', or None if already at end of list.
         """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        if pos.node.next is None:
            return None

        return Position(pos.node.next)

    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        return self._head.next.item
        

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise RuntimeError("Empty list")
        
        return self._tail.prev.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """    
        pos = self.front_pos()
        self.insert_before(pos,item)
        
    
    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        pos = self.front_pos()
        item: object = self.remove(pos)
        if isinstance(item,object):
            return
        else:
            raise RuntimeError("Error")

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        pos = self.back_pos()
        self.insert_after(pos, item)


    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        pos = self.back_pos()
        item = self.remove(pos)
        if isinstance(item,object):
            return
        else:
            raise RuntimeError("Error")


def main():
    a = DLList()
    pos = Position(a._tail)
    pos = a.insert_after(pos, 5)
    pos = a.insert_before(pos, 6)
    print(a)
    a.remove(pos)
    print(a.get_at(pos))
    print(a.remove(pos))
    print(a)
    # print(pos.node.item)
    # pos = a.insert_before(pos, 4)
    # print(a)
    # removed_ele = a.remove(pos)
    # print(removed_ele)
    # print(a)
    # b = a.insert_before(pos, 10)
    # print(a)
    # a.push_front(1)
    # a.push_front(2)
    # a.push_front(3)
    # pos = a.front_pos()
    # print(a.front())
    # print(a.back())
    # a.push_front(4)
    # print(a)
    # a.pop_front()
    # a.pop_front()
    # a.pop_front()
    # a.pop_front()
    # print(a)

    # a.push_back(4)
    # a.push_back(3)
    # a.push_back(2)
    # a.push_back(1)
    # print(a)

    # a.pop_back()
    # a.pop_back()
    # a.pop_back()
    # a.pop_back()
    # print(a)
    pass

if __name__ == "__main__":
    main() 
