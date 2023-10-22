# multilevel inheritance is for the one to another to another like grandfather to father to son

class grandfather:
    def gfather(self):
        print("Im the the Grandfather of this house")


class father(grandfather):
    def ffather(self):
        print("Im the the Father of this house ")


class ffather(grandfather):
    def ggfather(self):
        print("Im the bother of the father ")


class sonA(father):
    def sona(self):
        print("Im the the Son of this house")


class sonB(father):
    def sonb(self):
        print("Im the the Son of this house")


print("Manu---------------")
manu = sonB()
manu.ffather()
manu.gfather()
manu.sonb()

print("Tanu---------------")
tanu = sonA()
tanu.gfather()

print("Tau---------------")
print("father brother ")
tau = ffather()
tau.gfather()
print("---------------")
tanu.ggfather() #it will thorugh an error
