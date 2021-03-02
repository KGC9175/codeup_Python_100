n = int(input())
m = list(map(int, input().split()))
# lst = list(1, 3, 4)
# lst = [1, 3, 4]

m.reverse()
for i in m:
    print(i, end=" ")