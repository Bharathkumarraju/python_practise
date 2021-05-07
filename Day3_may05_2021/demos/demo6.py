

def fact(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial= factorial * i
    return factorial

def main():
    n = int(input("Please enter a number to findout its factorial"))
    factorial = fact(n)
    print("The factorial of {} is {}".format(n, factorial))


if __name__ == '__main__':
    main()