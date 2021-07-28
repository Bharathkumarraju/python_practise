square_dict = {}

for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

square_dict1 = { num: num*num  for num in range(1, 11)}
print(square_dict1)