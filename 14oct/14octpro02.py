# how to remove duplicate from list

my_list = [2,3,5,4,8,6,2,45,72,21,2]

#normal logic
arr = []
for i in my_list:
    if i not in arr:
        arr.append(i)
print(arr)
print()

# by set function
list2 = list(set(my_list))  #set is a funcation which is used for unorder and unique item
print(list2)