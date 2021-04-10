# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


r = int(input("please enter no of rows:"))


for i in range(r, 0, -1):  # 5 4 3 2 1
    for j in range(r-i+1):  # 0 1
        print(r-j, end=" ")
    print()
