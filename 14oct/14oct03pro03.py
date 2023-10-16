# finding two list are identical

list1 = [2, 3, 6, 4, 5]

list2 = [22, 3, 6, 4, 5]

if list1 == list2:
    print("Both are identically")
else:
    print("Both are non identically")


list3 = [9,8,7,6,5,4,3,2,1,0]
list4 = [4,0,1,2,3,4,5,6,7,8,9]

if len(list3)==len(list4):
    a = sorted(list3)
    b = sorted(list4)
    if a == b:
        print("Both are identically")
    else:
        print("Both are non identically")
else:print("Length are not same")