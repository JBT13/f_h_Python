class BinaryHeap:
    def __init__(self):
        self._data: list = []

    def __len__(self):
        return self._size
    def is_empty(self):
        return len(self._data) == 0

    def _parent_index(self, index: int) -> int:
        if index == 0:
            return 0
        return ((index - 1) // 2)


    def _last_child(self) -> int:
        if self.is_empty():
            raise IndexError
        return len(self._data) - 1


    def _add(self, value):
        if value is None:
            raise ValueError('element cannot be None')
        self._data.append(value)

    def _swap(self, child, parent):
        self._data[child], self._data[parent] = self._data[parent], self._data[child]

    def _heapify_up(self, child_index: int):
        """
        From last-node, as far up as needed, swap a node’s item with
        that of the parent if required to preserve the heap property.
        :return:
        """
        parent_index = self._parent_index(child_index)
        # IF child is greater than parent
        if self._data[child_index] < self._data[parent_index]:
            self._swap(child_index, parent_index)
            return self._heapify_up(parent_index)
        else:
            return True

    def _heapify_down(self, parent_index: int):
        left_index = 2*parent_index + 1
        right_index = left_index + 1
        small = parent_index
        # Using the fact that python optimizes and checking if first statement is true
        if left_index < len(self._data) and self._data[left_index] < self._data[small]:
            small = left_index
        if right_index < len(self._data) and self._data[right_index] < self._data[small]:
            small = right_index
        if small != parent_index:
            self._swap(parent_index, small)
            return self._heapify_down(small)

    def insert(self, value):
        self._add(value)
        last_child = self._last_child()
        self._heapify_up(last_child)
        return self._data
    def max(self):
        return self._data[0]

    def delete(self):
        if self.is_empty():
            raise IndexError('cannot delete an empty heap')
        self._swap(0, self._last_child())
        popped = self._data.pop()
        if not self.is_empty():
            self._heapify_down(0)
        return popped

    def __str__(self):
        return str(self._data)



test = BinaryHeap()
test.insert(5)
print(test)
test.insert(3)
print(test)
test.insert(1)
print(test)
test.insert(2)
print(test)
test.insert(20)
test.insert(5)
test.insert(100)
test.insert(5)
print(test)
print(test.delete())
print(test.delete())
print(test)