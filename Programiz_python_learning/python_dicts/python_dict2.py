my_dict = {'name': 'bharath', 'age': 33, "job": 'software developer'}

print(my_dict.keys())
print(my_dict.values())

print(my_dict.get('job'))
print(my_dict['name'])

# print(my_dict['location'])
print(my_dict.get('location')) # Just gives None

print("")
# print(my_dict['location']) Gives key Error

my_dict['address'] = 'singapore'
print(my_dict)
my_dict['hobby'] = 'learn python'
print(my_dict)



squares = {}

for num in range(1, 6):
    squares[num] = num * num
print(squares)

print(squares.pop(4))
print(squares)

print(squares.popitem())
print(squares)

squares.clear()
print(squares)

del squares