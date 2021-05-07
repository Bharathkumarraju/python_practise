a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

a_new = []

for i in a:
    a_new.append(is_even(i))

print(a)
print(a_new)