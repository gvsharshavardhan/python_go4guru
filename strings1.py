# a = "python"

# l = len(a)
# -6  -5  -4  -3  -2   -1
# p y t h o n
# 0 1 2 3 4 5

lang = input("enter sub name:")
topic = input("enter topic name:")
day = input("enter day:")

state = f"""
today we have {lang} session
we are gonna discuss about {topic}
and we will have next session on {day}
"""

print(state)
