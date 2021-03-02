w, h, b = map(int, input().split())
n = w*h*b
m = n/8/1024/1024

print('%.2f'%m, 'MB')