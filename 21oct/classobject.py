# class and object
# class always start with the capital letter

class Studentdata:
    # Data members
    Name = None
    Age = None
    Gender = None
    City = None

    # Method
    def do_quiz(self):
        print("Do something")

    def do_assignment(self):
        print("Do assignment")

Student1 = Studentdata()
Student1.do_quiz()
Student1.do_assignment()