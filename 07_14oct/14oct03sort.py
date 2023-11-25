# sorting the numbers

my_list = [78, 54, 84, 21, 48, 54, 94]
maximun = max(my_list)
# print(maximun)

# sorting the element
sorting = sorted(my_list)
print(sorting)
print(sorting[len(sorting) - 1])  # for last digit
print(sorting[len(sorting) - 2])  # for second last digit


# comparing the each element
# core logic function

def find_large_number(x):
    large_number = x[0]
    for n in x:
        if n > large_number:
            large_number = n
    return large_number


result = find_large_number(my_list)
print("my large number is ", result)
