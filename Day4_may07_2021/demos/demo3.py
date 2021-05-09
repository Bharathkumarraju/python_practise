list_a = [ 1, 3, 4, 6, 7, 8, 100]

smaller = 100
greater = 3

for i in list_a:
    if i < smaller:
        smaller = i
    if i > greater:
        greater = i

print(smaller)
print(greater)





