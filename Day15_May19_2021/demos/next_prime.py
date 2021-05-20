def main():
    n = int(input('Find the next prime number greater than: '))
    prime=find_next_prime(n, 2*n)
    print("next prime is: ", prime)

def find_next_prime(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

if __name__ == '__main__':
    main()