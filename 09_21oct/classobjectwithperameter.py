# passing parameter in class and object


class studentdata:
    name = None
    age = None
    email = None

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def nam(self):
        print("My name is " + self.name)

    def ag(self):
        print("My age is " + self.age)

    def emai(self):
        print("My email is " + self.email)


prateek = studentdata("prateek", "28", "psaxena49@gmail.com")
prateek.nam()
prateek.ag()
prateek.emai()
print()

priyanka = studentdata("priyanka", "25", "sachanp957@gmail.com")
priyanka.nam()
priyanka.ag()
priyanka.emai()