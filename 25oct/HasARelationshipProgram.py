# has a relation function
class grandfather:

    def gfather(self):
        print("grandfather")


class father:
    def ffather(self):
        grandfather().gfather()  # has a relation: where we are calling another function
        # super.__init__() this is used to call the parent class constructor
        print("has access")


manu = father()
manu.ffather()
