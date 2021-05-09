def largest_n(*args):
    list_b = args[0]
    n = args[1]
    list_b.sort()
    return(list_b[-n:])

def main():
    list_a = []
    for i in range(10):
        list_a.append(int(input("Enter {} value:  ".format(i + 1))))
    get_value = int(input("Enter the value "))
    get_n_largest = largest_n(list_a, get_value)
    print("The largest numbers in list are ", get_n_largest)

if __name__ == '__main__':
    main()