"""
1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1

1 = [0][0], [1][1], [2][2], [3][3]
2 = [1][0], [2][0], [2][1], [3][0], [3][1], [3][2]
0 = [0][1], [0][2], [0][3], [1][2], [1][3], [2][3]

"""

num = int(input("Enter n to print n * n array: "))

new_list=[]  # Initialising a new list

for i in range(num):
    new_list.append([])    # Creating a two dimensional array by adding new empty inner list
    '''
    Looping through the inner list and 
    comparing with the indexes of outer list and add the values for two dimensional array.
    '''
    for j in range(num):
        if i == j:
            new_list[i].append(1)
        elif i > j:
            new_list[i].append(2)
        else:
            new_list[i].append(0)
print(new_list)