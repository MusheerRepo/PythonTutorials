my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
my_dict["city"] = "New York"
print(my_dict.get("age"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.pop("age")
del my_dict["city"]
print(my_dict)

#Dictonary Comprehension
x = [{x : x +7} for x in range(5)]
print(x)