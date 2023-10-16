# Identity operators (is, is not )

a = 3
b = 3
print(a is b)

name1 = "Prateek"
name2 = "prateek"
print(name1 is not name2)

# In list is never be equal but it position number can be equal
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1[0] is list2[0])