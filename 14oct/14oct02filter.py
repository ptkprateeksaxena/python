# find the even number with the help of list

list_m = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x):
    return x % 2 == 0


even_number = filter(is_even, list_m)
print(even_number)
even_number = list(even_number)
print(even_number)
