
"""
2 rows
3 colums

[
[1, 2, 3]
[4, 5, 6]
]

"""
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))
new_list = []

for i in range(rows):
    new_list.append([])
    for j in range(cols):
        new_list[i].append(j)
print(new_list)

