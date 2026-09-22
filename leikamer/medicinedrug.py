import math

n, k, l = map(int, input().split())

need = n * k

pack = math.ceil(need / l)

print(pack)