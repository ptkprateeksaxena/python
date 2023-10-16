'''1. Say Hello
2. Choose another
3. Quit'''

choose = None

while choose != "3":
    Number = input("Enter Your number ")
    if Number == "1":
        print("Hello World")
    elif Number == "2":
        print(" Choose another number ")
    elif Number == "3":
        print("Quit")
        break
    else: print("Enter valid Number ")
print("End")