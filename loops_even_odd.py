# r = range(5)  # 01234
# print(r, type(r))


# 45 to 67
start = int(input("give me start number:"))
stop = int(input("give me stop number:"))
for i in range(start, stop):
    if i % 2 == 1:
        print(i)
