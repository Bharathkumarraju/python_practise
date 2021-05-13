'''
1
22
333
4444
55555
'''

"""
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print("")
"""

"""
k = 1
for i in range(1,6):
    for j in range(i):
        print(k, end="")
    print("")
    k = k + 1
"""

'''
11111
2222
333
44
5
'''

"""
for i in range(5, 0, -1):
    for j in range(i):
        print(6 - i, end="")
    print("")
"""

"""
k = 1
for i in range(5, 0, -1):
    for j in range(i):
        print(k, end="")
    print("")
    k = k + 1
"""

'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''


for i in range(6, 1, -1):
    for j in range(i):
        print(j, end="")
    print("")

print("--------------------------")

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end="")
    print("")

print("--------------------------")

k = 5
for i in range(5, 0, -1):
    for j in range(i):
        print(k, end="")
    print("")
    k = k - 1