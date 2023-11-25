# single inherintance
# when child class have permission to access property of parent class

class a:
    def hod_a(self):
        print("parent class")


class b(a):
    def ho_b(self):
        print("child class")


obj = b()
obj.ho_b()
obj.hod_a()
