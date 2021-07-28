num = int(input("Enter an integer: "))


for number in range(num, 0, -1):
    print("--------The Multiplication table for {} ---------".format(number))
    for count in range(1, 11):
        print(number, "x", count, "=", number * count)