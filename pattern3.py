"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
r = int(input("please enter no of rows:"))

for i in range(r):  # 0 1 2 3 4
    for j in range(i+1):  # 1 0
        print(j+1, end=" ")
    print()

# note:
# outer loop -> rows
# inner loop -> columns
