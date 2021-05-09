list_a = [ 9, 8, 1, 3, 56, 676]
list_b = []
max = 0

for i in range(len(list_a)):
    if list_a[i] > max:
        max = list_a[i]
print(max)

list_b.append(max)
print(list_b)
