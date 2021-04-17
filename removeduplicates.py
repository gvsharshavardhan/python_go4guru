# a1a,a? bcd a,ab1b?d
# abcd, ?1

box1 = input("enter some text:")

box2 = ""

for i in box1:
    if i not in box2:
        box2 = box2 + i
print(box2)
