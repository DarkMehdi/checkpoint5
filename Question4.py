class bank:
    def __init__(self,money):
        self.money=money
    def add (self):
        a=int(input("value:"))
        if a < self.money :
            print("not enough money!!")
        else:
            self.money += a
            print(self.money)

    def taken (self):
        t=int(input("value:"))
        if t > self.money :
            print("not enough money!!")
        else:
            self.money -= t
            print(self.money)
mybank=bank(0)
while True:
    i = input("What do you want to do (add/take/quit)?  ")
    if i == "add":
        mybank.add()
    elif i == "take":
        mybank.taken()
    elif i == "quit":
        print("bye!!")
        break
    else:
       print("error")
       continue