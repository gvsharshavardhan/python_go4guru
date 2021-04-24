
# i/p: a4b4c2a2
# o/p: aaaabbbbccaa


input = input("enter some seq: ")
l = len(input)
temp = ""
for i in range(l):
    if input[i].isdigit():
        temp += input[i-1]*int(input[i])

print(temp)
