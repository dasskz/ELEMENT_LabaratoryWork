a = int(input())
b = int(input())
n = ""
if a <= b:
    for i in range (a, b+1):
        if i % 2 == 0:
            n = n + str(i) + " "
    print(n)
else: print("Error")
