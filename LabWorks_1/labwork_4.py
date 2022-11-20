a = int(input())
b = a // 2 * 5
c = (a-1) // 2 * 15
d = 9 * 60 + a * 45 + b + c
print(f'{d//60} {d%60}')