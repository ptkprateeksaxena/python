# Class and Object for car
# DM: carname, carcolor, carmodel
# method: start, carnumber
# maruti, tesla
class car:
    name = None
    color = None    #these are the data member
    model = None

    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def start(self):
        print(" Car start " + self.name)

    def colo(self):
        print(" Car color " + self.color)

    def mode(self):
        print(" Car model name " + self.model)

    # def pri(self):
    #     print(self.name, self.model, self.color)



maruti = car("Maruti", "red", "aulto")
maruti.start()
maruti.colo()
maruti.mode()
print()
print()

Tesla = car("Tesla", "red", "Truck")
Tesla.start()
Tesla.colo()
Tesla.mode()
print()
print()

tata = car("Tata", "Green", "Punch")
tata.start()
tata.colo()
tata.mode()
print()

x = 0
while x<3:
    car_name = input("Enter the car name ")
    car_color = input("Enter the car color ")
    car_model = input("Enter the car model ")

    cartype = car(car_name, car_color, car_model)
    cartype.start()
    cartype.colo()
    cartype.mode()

    x+=1