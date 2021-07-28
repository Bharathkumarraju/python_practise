num = int(input("Enter  a number: "))
sum = 0

for i in range(1, num + 1):
    sum = sum + i
print("The sum of numbers till {} is {}".format(num, sum))