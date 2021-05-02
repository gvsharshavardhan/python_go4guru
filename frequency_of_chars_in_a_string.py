name = "harsha vardhan"
# s_name = set(name)
# d = {}
# for char in s_name:
#     d[char] = name.count(char)
# print(d)
d = {}
for char in name:
    d[char] = d.get(char, 0)+1
print(d)
