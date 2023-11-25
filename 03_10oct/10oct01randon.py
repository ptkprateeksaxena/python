import random
lucky_no = random.randint(0,9)
guess_no = None

while guess_no != lucky_no:
    guess_no = int(input("Enter your lucky number "))
    if (guess_no > lucky_no):
        print("Your number is greater ")
    elif (guess_no < lucky_no):
        print("Your number is smaller then lucky number")
print("Your find the lucky number", lucky_no)