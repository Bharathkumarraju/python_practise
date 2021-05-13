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

print("")

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end="")
    print("")
