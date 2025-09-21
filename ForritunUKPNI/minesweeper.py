m, n, k = map(int, input().split())


grid = [['.' for _ in range(n)] for _ in range(m)]

for _ in range(k):
    a, b = map(int, input().split())
    grid[a - 1][b - 1] = '*' ## due to indexing [1, 1] = first row first column
 
for row in grid:
    print(''.join(row))
