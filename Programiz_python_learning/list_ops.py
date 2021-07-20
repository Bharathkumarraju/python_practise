a = [ 1 , 3, 5, 7]

a_new = [x ** 2 for x in a ]
print(a_new)

b = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    if num %2 == 0:
        return num
    else:
        pass

b_new = []

for i in b:
    if is_even(i) == i:
        b_new.append(is_even(i))

print(b_new)