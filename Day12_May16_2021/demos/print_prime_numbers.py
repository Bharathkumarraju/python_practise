def check_prime(n):
    is_prime = True
    for i in range(2,n):   # 2,9
        if n % i == 0:
            is_prime = False
    return is_prime


def prime(m, n):
    prime_list = []
    for i in range(m, n+1): # 5,6,7,8,9,10(2, 500)
        is_prime = True
        for j in range(2, i//2+1):
            if i % j == 0:  # 6 % 2, 3, 4, 5,
                is_prime = False
                break
        if is_prime == True:
           prime_list.append(i)
    return prime_list

def main():
    m, n = int(input("Enter inital value")),int(input("Enter end value"))
    get_primes = prime(m, n)
    print("the primes are ", get_primes)

    # n = int(input("Enter a number"))
    # get_prime = check_prime(n)
    # if get_prime == True:
    #     print("the numeber is prime")
    # else:
    #     print("the number is not prime")


if __name__ == '__main__':
    main()







