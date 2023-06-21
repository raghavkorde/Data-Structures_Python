
num1 = 11
num2 = num1
#both point to same memory location
print(f"id of num1: {id(num1)} == id of num2: {id(num2)}")

num2 = 22
#as soon as num2 is reassigned to a fixed value, it no longer points to num1
print(f"id of num1: ${id(num1)} != id of num2: ${id(num2)}")

# num1 and num2 are now separate objects residing in different memory locations. 
# integers in Python are immutable, so when you assign a new value to a variable, 
# it creates a new object rather than modifying the existing one. 

dict1 = {'key' : 11}
dict2 = dict1

#both point to same memory location
print(f"id of dict1: {id(dict1)} == id of dict2: {id(dict2)}")

dict2['key'] = 22

print(f"dict1['key'] = {dict1['key']} which is same as dict2['key']")
print(f"This is because, id of dict1: {id(dict1)} == id of dict2: {id(dict2)}")

# dictionary in python is mutable
# It's important to note that this behavior is specific to mutable objects 
# like dictionaries, lists, sets, etc. Immutable objects like integers, strings,
# and tuples behave differently, as shown in the previous explanation regarding integers.
