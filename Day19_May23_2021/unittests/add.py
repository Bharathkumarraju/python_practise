def add(a, b):
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError
    if isinstance(a, complex) or isinstance(b, complex):
        raise TypeError
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError
    result = a + b
    return result

def main():
    a = int(input("enter a value: "))
    b = int(input("enter b value: "))
    sum = add(a, b)
    print("The sum of {} , {} is {}".format(a, b, sum))

if __name__ == '__main__':
    main()