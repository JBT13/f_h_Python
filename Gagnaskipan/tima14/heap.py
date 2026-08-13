class PQMinList:

    def __init__(self):
        self._data = []

    def push(self, element: int) -> None:
        self._data.append(element)
        self.heapify_up(len(self._data)-1)

    def pop(self) -> int:
        if self.size() == 0:
            return None
        
        root = self._data[0]
        last = self._data.pop()

        if self.size() > 0:
            self._data[0] = last
            self.heapify_down(0)

        return root 

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty PQ")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def copy(self) -> "PQMinList":
        mh = PQMinList()
        mh._data = self._data[:]  # shallow copy is sufficient as we are only working with 
        return mh                 # non-mutable data (int).

    def heapify_up(self, index):
        parent = (index - 1) // 2

        if index > 0 and self._data[index] < self._data[parent]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            self.heapify_up(parent)

    def heapify_down(self,index):
        small = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self._data) and self._data[left] < self._data[small]:
            small = left

        if right < len(self._data) and self._data[right] < self._data[small]:
            small = right

        if small != index:
            self._data[index], self._data[small] = self._data[small], self._data[index]
            self.heapify_down(small)


n = int(input())
dic = {}

for _ in range(n):
    ls = input().split()
    a = int(ls[0])  
    b = ls[1]

    if b == "a":
        target_id = int(ls[2])
        if target_id in dic:

            dic[a] = dic[target_id].copy()
        else:
            dic[a] = PQMinList()
        continue 

    if a not in dic:
        dic[a] = PQMinList()

    if b == "+":
        val = int(ls[2])
        dic[a].push(val)

    elif b == "-":
        dic[a].pop()

    elif b == "p":
        print(dic[a].peek())

    elif b == "s":
        print(dic[a].size())