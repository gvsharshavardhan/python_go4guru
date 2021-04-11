currntamt = 500

flag = True
trail = 0

while flag:
    trail += 1
    username = input("please enter your user name:")
    password = input("please enter your password:")
    if(username.lower() == "harsha" and password == "password123"):
        withdrawamt = int(input("please enter some amt to withdraw:"))
        if withdrawamt > currntamt:
            print("your withdraw amt is more than current balance, you cannot withdraw!!")
        else:
            currntamt = currntamt-withdrawamt
            print("amt wothdrawn succesfully!")
            print("your current balance is : ", currntamt)
        break
    else:
        print("please check your credentiuals!!")
        print("you have {} more trails".format(3-trail))
        if(trail == 3):
            break
