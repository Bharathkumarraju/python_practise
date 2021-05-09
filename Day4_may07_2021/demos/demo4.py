list_a = [10, 35, 25, 6, 8, 1, 2]

smaller = 10
bigger = 6

for i in list_a:
    if i < smaller:
        smaller = i
    if i > bigger:
        bigger = i

print(smaller)
print(bigger)

