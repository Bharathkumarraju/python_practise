my_dict = {'name': 'bharath', 'age': 33, "job": 'software developer'}

print(my_dict.keys())
print(my_dict.values())

print(my_dict.get('job'))
print(my_dict['name'])

# print(my_dict['location'])
print(my_dict.get('location')) # Just gives None

print("")
# print(my_dict['location']) Gives key Error