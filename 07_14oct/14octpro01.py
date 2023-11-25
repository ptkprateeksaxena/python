#how to find the list is empty or not

my_list = [5]
my_list1 = []
my_list2 = [5,8,45,25,458]

empty_list = len(my_list)
if empty_list == 0:
   print("The list is empty")
else:print("list is not empty")

def checklist(x):
    if len(x)==0:
        print("List is empty ", x)
    else:print("list is not empty ",x)

checklist(my_list)
checklist(my_list1)
checklist(my_list2)