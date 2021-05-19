
def prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    return is_prime


def main():
 #   num = int(input("Enter a number: "))
    num = 19
    get_prime = prime(num)
    if get_prime == True:
        print("Entered number i.e. {} is prime number".format(num))
    else:
        print("Entered number i.e. {} is not a prime number".format(num))


if __name__ == '__main__':
    main()