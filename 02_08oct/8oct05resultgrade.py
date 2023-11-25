Marks = int(input("Enter your marks "))
print("Your marks is ", Marks)
if (Marks <= 33):
    print("Your grade is E")
elif (Marks >= 33 and Marks <= 40):
    print("Your grade is E+")
elif (Marks >= 41 and Marks <= 50):
    print("Your grade is D")
elif (Marks >= 51 and Marks <= 60):
    print("Your grade is D+")
elif (Marks >= 61 and Marks <= 70):
    print("Your grade is c")
elif (Marks >= 71 and Marks <= 80):
    print("Your grade is C+")
elif (Marks >= 81 and Marks <= 90):
    print("Your grade is B")
elif (Marks >= 91 and Marks <= 100):
    print("Your grade is A+")
else:
    print("Enter valid marks")
