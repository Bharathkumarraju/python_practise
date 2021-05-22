try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    res = a / b
    print(res)

    my_list = [1, 2, 3]
    i = int(input("enter index: "))
    print(my_list[i])

except ZeroDivisionError:
    print("Divide by 0 is not posiible, try again!!!")

except IndexError:
    print("Index can not be greater than size of a list")

print("program ends")