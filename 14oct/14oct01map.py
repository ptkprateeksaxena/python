''' map and filter in this program
map will apply function(double_list) to each element of the list
'''

list = [2, 3, 4, 5, 6]


def double_list(a):
    return a * 2


result = map(double_list, list)
print(result)

for i in result:
    print(i)