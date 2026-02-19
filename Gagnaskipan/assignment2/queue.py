#
# Gagnaskipan.
# Deque implementation
# Student(s):
#  - ... your name ...
#
from sll import SLList

class Queue:
    def __init__(self, lst):
        """"
        Constructor.
        """
        self._lst = lst


    def __len__(self):
        """"
        Returns the number of elements in the queue.
        """
        return len(self._lst)

    def __str__(self):
        """
        Returns the string representation of the queue.
        """
        return str(self._lst)

    def is_empty(self):
        """
        Returns True if queue is empty, otherwise False.
        """
        return self._lst.is_empty()

    def front(self):
        """
        Returns the front element of the queue (without removing it).
        :return: If non-empty, the front element of the queue, otherwise throws exception.
        """
        return self._lst.front()

    def enqueue(self, item):
        """
        Inserts the element to the back of the queue.
        """
        return self._lst.push_back(item)

    def dequeue(self):
        """
        Removes the element at the front of the queue (without returning)..
        """
        return self._lst.pop_front()


def main():
    a = SLList()
    que = Queue(a)
    print(que)
    que.enqueue(1)
    print(que)
    que.enqueue(2)
    que.enqueue(3)
    print(que)
    que.dequeue()
    print(que)
    que.dequeue()
    que.dequeue()
    print(que)
    print(que.is_empty())
    que.enqueue(42)
    print(que.front())


if __name__ == "__main__":
    main()
