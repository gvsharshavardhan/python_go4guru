# k l m n o
# g h i j
# d e f
# b c
# a

rows = int(input("enter row count:"))

start = ord("a")
last = start - 1 + int((rows*(rows+1))/2)
temp = ""
for i in range(rows, 0, -1):
    for j in range(i):
        temp += chr(last)
        last -= 1
    print(temp[::-1])
    temp = ""
