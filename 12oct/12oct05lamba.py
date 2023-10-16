# 1
def numqw(num):
    return num * 3


print(numqw(9))

# 2
test = lambda you: you * 10

print(test(5))

# 3  create a program which take user input and do 2^numm

user_input = int(input("Enter the number: "))

result = lambda a: pow(2, a)  # a**2
print(result(user_input))

user_inputa = int(input("Enter the number: "))

results = lambda a,b: sum(a,b) # a**2
print(results(user_input,user_inputa))
