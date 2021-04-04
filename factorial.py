# 5 -> 5*4*3*2*1

n = int(input("please enter a number:"))

total = 1

for i in range(n, 0, -1):
    total *= i

print(total)
