# coverting json to dict
import json

my_json_data = '{"name":"prateek", "age":32 , "city":"bly"}'
print(type(my_json_data)) #json always have a value in str

py_json = json.loads(my_json_data)
print(py_json)
print(type(py_json))
print(py_json["name"])
print(py_json["age"])
print()
print(py_json.keys())
print(py_json.values())
print(py_json.items())