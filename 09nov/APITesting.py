import requests


def res():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1284")
    print(response.text)
    print(response.status_code)
    if response.status_code == 200:
        print("#TC1 Pass succesfull")

for i in range(10):
    res()
    print(i)