"""
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""

r = int(input("no of rows:"))
c = int(input("no of coloumns:"))


myord = ord("A")  # 100

for i in range(r):  # 0 1 2 3 4
    for j in range(c):  # 0 1 2 3 4
        print(chr(myord+i), end="")
    print()
