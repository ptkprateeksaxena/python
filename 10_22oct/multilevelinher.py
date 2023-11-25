# multilevel inheritance is for the one to another to another like grandfather to father to son

class grandfather:
    def gfather(self):
        print("Im the the Grandfather of this house")


class father(grandfather):
    def ffather(self):
        print("Im the the Father of this house")


class son(father):
    def son(self):
        print("Im the the Son of this house")

manu = son()
manu.son()