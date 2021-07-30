dict1 = {}
for k1 in range(11, 14):
    dict1[k1] = {}
    for k2 in range(1, 4):
        dict1[k1][k2] = k1 * k2
print(dict1)


# In dictionary nested comprehension first inner loop getting executed

dict2 = {  k1: {k2: k1* k2 for k2 in range(1, 6) } for k1 in range(2, 5) }
print(dict2)