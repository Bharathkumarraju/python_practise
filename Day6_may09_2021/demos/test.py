N = 2

list_a = [5, 2, 4, 8, 7, 10]
list_b = []
for i in range(0, N):
    max = 0
    for j in range(len(list_a)):
        if list_a[j] > max:
            max = list_a[j]
#    list_a.remove(max)
    list_b.append(max)
    print(list_b)