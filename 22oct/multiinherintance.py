# In multi inherintance child class have access to multiple parent class

class a():
    def parta(self):
        print("this is class a")

    def subs(self):
        print("this is copy class A")

class b():
    def partb(self):
        print("this is class b")

    def subs(self):
        print("this is copy class B")

class c(a,b):
    def partc(self):
        print("this is class c")
tanu = c()
tanu.partb()
tanu.partc()
tanu.parta()
tanu.subs() # this is bcz of MRO method resolution order