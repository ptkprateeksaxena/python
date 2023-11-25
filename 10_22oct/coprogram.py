class mobilephone:
    company_name = None
    model_name = None
    model_color = None

    def __init__(self, a, b, c):
        self.company_name = a
        self.model_name = b
        self.model_color = c

    def mode(self):
        print("Your Mobile name is: " + self.company_name)

    def mod(self):
        print("Your Mobile model is: " + self.model_name)

    def mo(self):
        print("Your Mobile color is: " + self.model_color)


company = input("Enter the mobile company name: ")
model = input("Enter the mobile company model: ")
color = input("Enter the mobile color: ")
nokia = mobilephone(company, model, color)
nokia.mode()
nokia.mod()
nokia.mo()
