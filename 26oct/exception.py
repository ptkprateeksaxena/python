# Exception:- it is an event that occurs during the execution of the program that disturb the normal flow the instruction
#
# x = int(input("the the number: "))
# Result = 10 / x
# print(Result)

'''
conditions:

* divided by zero               --> ZeroDivisionError: division by zero
* String or nothing             --> ValueError: invalid literal for int() with base 10: 'sdfs'
* negative value                --> Fine
* None                          --> ValueError: invalid literal for int() with base 10: 'None'
* Fload                         --> ValueError: invalid literal for int() with base 10: '12.5'
* Complex number                --> ValueError: invalid literal for int() with base 10: '8+5j'
* Alphanumeric : ABC123         --> ValueError: invalid literal for int() with base 10: 'abc123'
* large number: 9999999         --> Fine
* boolean: True or Flase        --> ValueError: invalid literal for int() with base 10: 'True'
* special character:!@#$%^&*()  --> ValueError: invalid literal for int() with base 10: '!@#'
* list dir: (), {}, []          --> ValueError: invalid literal for int() with base 10: '[2,5,7]'

'''
try:
    number = int(input("the the number: "))
    Result = 10 / number
    print("Result" + Result)
# except ZeroDivisionError as Error:
#     print("Enter a valid number1: ", Error)
# except ValueError as Error:
#     print("Enter a valid number2: ", Error)
# except TypeError as Error:
#     print("Enter a valid number3: ", Error)
# except SyntaxError as Error:
#     print("Enter a valid number5: ", Error)
# except NameError as Error:
#     print("Enter a valid number4: ", Error)
except Exception as Error:
    print("Parent Error ", Error)
finally:
    print("Thank you")






















































