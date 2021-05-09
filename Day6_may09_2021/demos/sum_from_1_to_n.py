# sum of N numbers

# n = 5
# n + (n - 1)

# 1. Stopping condition
# 2. Recursive condition

def sum_of_natural(n):
    if n == 1:
        return 1
    else:
        return(n + sum_of_natural(n - 1))

def main():
    n = int(input("Enter a Value: "))
    sum_of_n = sum_of_natural(n)
    print("Sum of {} numbers is: {} ".format(n, sum_of_n))


if __name__ == '__main__':
    main()