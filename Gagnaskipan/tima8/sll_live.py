class Node:
    def __init__(self, data=None, next=None, prev= None):
        self.data = data
        self.next= next
        self.prev = prev
    
    def __bool__(self):
        return self.data is not None


class DLL_Deque:
    def __init__(self):
        self.head = Node(prev="Sentinel")
        self.tail = Node(next="Sentinel")
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = 0

    def __str__(self) -> str:
        result = ''
        if self.size == 0: 
            return f"[{result}]"
        
        current_node: Node = self.head.next
        while current_node:
            result += str(current_node.data) + ', '
            current_node = current_node.next
         
        return result[:-2]
    
    def push_front(self, elem):
        behind: Node = self.head.next
        new_node = Node(elem, behind, self.head)
        self.head.next = new_node
        behind.prev = new_node
        self.size += 1

    def push_back(self, elem):
        front: Node = self.tail.prev
        new_node = Node(elem, self.tail, front)
        self.tail.prev = new_node
        front.next = new_node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError("This cannot be")

        value = self.head.next
        new_head: Node = self.head.next.next
        new_head.prev = self.head
        self.head.next = new_head
        self.size -= 1

        a = value
        del value
        return a

    def pop_back(self):
        if self.size == 0: # edge case: list is empty
            raise IndexError("This cannot be")
        
        value = self.tail.prev
        new_tail: Node = self.tail.prev.prev
        new_tail.next = self.tail
        self.tail.prev = new_tail
        self.size -= 1

        a = value
        del value
        return a

a = DLL_Deque()
a.push_front(1)
print(a)
a.push_front(2)
print(a)
a.push_back(4)
print(a)
a.push_back(5)
print(a)
a.pop_back()
print(a)
a.pop_front()
print(a)