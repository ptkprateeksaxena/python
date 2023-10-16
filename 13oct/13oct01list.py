# build in list function

num = [1, 2, 3, 4]
print(num)
print(num[1])

# slicing

print(num[0:3])
print(num[2:4])
print(num[:])
print(num[-1:])
print(num[:-1])

# append
num.append(5)
print(num)

# extend
num.extend([6])
print(num)

# insert
num.insert(1, 5)
print(num)

# remove
num.remove(5)
print(num)

# pop: remove a perticular item from the list
i = num.pop(4)
print(i)
print(num)

#len
print(len(num))

#count: to show number to times iteam appear in the list
print(num.count(5))