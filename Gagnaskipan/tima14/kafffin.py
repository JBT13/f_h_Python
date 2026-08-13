class PQMaxlist:

    def __init__(self):
        self._data = []

    def push(self, element: int) -> None:
        self._data.append(-element)
        index = len(self._data) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                index = parent
            else:
                break

    def pop(self) -> int:
        if not self._data: return None
        root = -self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            index = 0
            while True:
                small = index
                left = 2 * index + 1
                right = 2 * index + 2
                if left < len(self._data) and self._data[left] < self._data[small]:
                    small = left
                if right < len(self._data) and self._data[right] < self._data[small]:
                    small = right
                if small != index:
                    self._data[index], self._data[small] = self._data[small], self._data[index]
                    index = small
                else:
                    break
        return root

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty PQ")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def copy(self) -> "PQMaxlist":
        mh = PQMaxlist()
        mh._data = self._data[:]  # shallow copy is sufficient as we are only working with 
        return mh                 # non-mutable data (int).


n = int(input())

task = []
for _ in range(n):
    task.append(list(map(int,input().split())))

task.sort(key = lambda x: x[1])

heap = PQMaxlist()

total = 0
drinks = 0

for time, deadline in task:
    total += time
    heap.push(time)

    while total > deadline:
        big = heap.pop()
        new = big // 2
        minus = big - new 

        total -= minus
        heap.push(new)
        drinks += 1

print(drinks)
