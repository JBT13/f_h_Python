class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Keeps track of tree height

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Attach smaller rank tree under higher rank tree
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

n, m = map(int, input().split())

union = UnionFind(n) 

for _ in range(m):
    a, b = map(int, input().split()) 
    union.unite(a,b) 
    print(union.parent)


print(union.parent)      
