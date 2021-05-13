'''
5
1,5
'''

def prime(n):
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            return False
    return True


def main():
    n = int(input("Enter a Number to find out its prime or not"))
    prime_number = prime(n)
    if prime_number == True:
        print("The enetered number is prime")
    else:
        print("Not a prime")


if __name__ == '__main__':
     main()