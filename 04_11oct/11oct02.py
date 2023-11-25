# finding positive and negative number with the help of match, case and if

num = int(input("Enter the number "))

match num:
    case 0:
        print(" Your number is ZERO")
    case num if num > 0:
        print("Your number is positive ", num)
    case num if num < 0:
        print("Your number is negative ", num)
    case _: print("invalid number")
