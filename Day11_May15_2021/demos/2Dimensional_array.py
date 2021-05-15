def n_dimensional_array(n):
    new_array = []
    for i in range(n):
        new_array.append([])
        for j in range(n):
            new_array[i].append(i*2)
            new_array[i][j] = i + 3
    return new_array

def main():
    n = int(input("Enter a number to display array: "))
    n_array = n_dimensional_array(n)
    print("the 2 dimensional array is {}".format(n_array))


if __name__ == '__main__':
    main()

