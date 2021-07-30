squares = {i: i*i for i in range(10)}
print(squares)

squares_odd = {i: i*i  for i in range(10) if i % 2 == 1}
print(squares_odd)

print(2 in squares_odd)

for i,j in squares_odd.items():
    print(i,j)

for k in squares_odd:
    print(squares_odd[k])


print(all(squares_odd))
print(all(squares))