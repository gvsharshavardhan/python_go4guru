brackets = {"(": ")", "[": "]", "{": "}"}

data = "()"

stack = []

for bracket in data:
    if bracket in brackets:
        stack.append(bracket)
    else:
        open_bracket = stack.pop()
        if brackets[open_bracket] == bracket:
            continue
        else:
            break
if len(stack) == 0:
    print("balanced!")
else:
    print("not balanced!!")
