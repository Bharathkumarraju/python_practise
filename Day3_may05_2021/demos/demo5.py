a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

a_new = []
b_new = []

for i in a:
    a_new.append(is_even(i))

b_new = [is_even(x) for x in a]  # list comprehension


print(a)
print(a_new)
print(b_new)