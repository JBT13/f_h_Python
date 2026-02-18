class Node:
    def __init__(self, data:object = None, next = None):
        self.data = data
        self.next = next

    def __bool__(self):
        return self.data is not None


def push_front(head: Node, item):
    if not head:
        return Node(item)

    return Node(item, head)

def print_values(head: Node):
    while head:
        print(head.data)
        head = head.next

def remove_first(head: Node):
    old_head = head 
    new_head = head.next
    del old_head
    return new_head

