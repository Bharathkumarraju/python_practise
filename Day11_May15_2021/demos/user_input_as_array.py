# new_list = []
#
# for i in range(9):
#     new_list.append(int(input("Ener {} value: ".format(i + 1))))
# print(new_list)
#
# list_a=[]

#rows
#cols
'''
1 1 1
1 1 1
1 1 1

[[1,1,1][1,1,1],[1,1,1]]
'''

new_list = []
for i in range(3):
    new_list.append([])
    for j in range(3):
        new_list[i].append(int(input("enter a value")))
print(new_list)