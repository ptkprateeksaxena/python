# this program is to knowledgr the match and case

Name = input("Enter your name: ")

match Name:
    case "Prateek":
        print("this is Prateek")
    case "prateek":
        print("your name is prateek")
    case "prateeK":
        print("wrong name")
    case _: print("invalid input")
print("end")
