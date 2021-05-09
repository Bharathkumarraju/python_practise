def find_largest_Ns(*args):
    list_b = args[0]
    final_list = []
    n = args[1]
    for i in range(0, n):
        max = 0
        for j in range(len(list_b)):
            if list_b[j] > max:
                max = list_b[j]
        list_b.remove(max)
        final_list.append(max)
    return(final_list)

def main():
    list_a = []
    for i in range(7):
        list_a.append(int(input("enter {} element: ".format(i + 1))))
    get_number = int(input("Enter a number to print those many largest numbers in a list"))
    largest_number = find_largest_Ns(list_a, get_number)
    print("The {} largest numbers in a list are {} ".format(get_number, largest_number))

if __name__ == '__main__':
    main()