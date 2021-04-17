name = input("enter some text:")

print(name[::-1])

l = len(name)
rev = ""
for i in range(l-1, -1, -1):
    rev = rev + name[i]

print(rev)

if(name == rev):
    print("palindrome")
else:
    print("not palindrome")
