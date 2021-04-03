age = int(input("please enter your age: "))
if age > 0:
    if age > 60:
        print("old age!!")
    elif age > 30 and age <= 60:
        print("middle age!!")
    elif age > 12 and age <= 30:
        print("young age!!")
    else:
        print("kids!")
else:
    print("age cannot be zero or -ve!!")

# 80 -> old age
# 45 -> middle age
# 25 -> young age
# 6 -> kids
# 60 -> middle age
# 30 -> young age
# 12 -> kids
# -ve or 0 -> age cannot be zero or -ve
