intial_string = "python is a easy language"

l_w = intial_string.split()

final_string = ""

for index in range(len(l_w)):  # 0 1 2 3 4
    if index % 2 == 1:
        final_string += l_w[index][::-1]
    else:
        final_string += l_w[index]
    final_string += " "
print(final_string)
