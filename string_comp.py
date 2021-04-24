# o/p: a4b4c2a2
# i/p: aaaabbbbccaa

input = input("enter some seq: ")
l = len(input)
temp = ""
counter = 1
for i in range(1, l):
    if input[i] == input[i-1]:
        counter += 1
    else:
        temp += input[i-1]+str(counter)
        counter = 1
temp += input[i]+str(counter)
print(temp)
