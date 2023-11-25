# Dictonary is a collection of a key and value. it comes in {}
# json is used to store the data, similarry is dictonary
# no duplicate keys

my_dict = {"name": "prateek", "age": 25}
print(my_dict)
print(type(my_dict))

# Access the value
print(my_dict["age"])

# replace the value
my_dict["name"] = "Saxena"
print(my_dict)

# add new key and value
my_dict["city"] = "Bareilly"
print(my_dict)

# delete key value pair
del my_dict["age"]
print(my_dict)

# list, tuple, set
my_dict1 = {"l_name": ["raghu", "raju", "raja"], "l_city": ["Bareilly", "subhash nagar"]}
my_dict2 = {"t_name": ("Ram", "Sita", "lakshman"), "t_city": "subhash nagar"}
print(my_dict1)
print(my_dict2)

#dict in dict

