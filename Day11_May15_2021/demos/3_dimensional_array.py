list_a=[]

"""
[
[ [1,1,1] ]
]
3 * 3 * 3
"""

for i in range(3):
    list_a.append([])
    for j in range(3):
        list_a[i].append([])
        for k in range(3):
            list_a[i][j].append(1)

print(list_a)