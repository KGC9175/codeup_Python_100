a, r, n = map(int, input().split())
m = a

for _ in range(1, n):
    m = m * r 

print(m)