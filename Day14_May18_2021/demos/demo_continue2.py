for i in range(1, 6):
    num = float(input("Enter {} number: ".format(i)))
    if num < 0:
        continue
    print("Entered number is: ", num)
