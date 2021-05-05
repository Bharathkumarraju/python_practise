def sum_of_numbers(j):
    sum = 0
    for i in range(1, j + 1, 1):
        sum = sum + i
    return sum

def main():
    n = int(input("Enter the number to calculate the sum upto it!!!"))
    sum_is = sum_of_numbers(n)
    print("the sum of numbers until {} are {}".format(n, sum_is))


if __name__ == '__main__':
    main()