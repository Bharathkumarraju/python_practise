def getsum(n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum

def main():
    list_one = []
    for i in range(5):
        list_one.append((int(input("Enter the {} value".format(i + 1)))))
    sum_of_values = getsum(list_one)
    print("The sum of list values are {}".format(sum_of_values))


if __name__ == '__main__':
    main()