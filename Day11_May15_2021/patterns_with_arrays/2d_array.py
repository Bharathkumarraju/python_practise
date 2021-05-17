"""
[[2, 2, 2], [2, 2, 2], [3,3,3]]

[[2,3,5], [6, 7, 8], [4,5,6]]

"""

def create_2d_array(rows, cols):
    list_a = []
    for i in range(rows):
        list_a.append([])
        for j in range(cols):
            list_a[i].append(int(input("Enter {} value for {} th row".format(j + 1, i + 1))))
    return list_a

def matrix_addition(x, y):
    matrix_sum = []
    if (len(x) == len(y)) and (len(x[0]) == len(y[0])):
        for row in range(len(x)):
            matrix_sum.append([])
            for col in range(len(x[0])):
                matrix_sum[row].append(x[row][col] + y[row][col])
        return matrix_sum

def main():
    get_2d_array = create_2d_array(3, 3)
    print(get_2d_array)
    get_2d_array_2 = create_2d_array(3, 3)
    print(get_2d_array_2)
    add_matrix = matrix_addition(get_2d_array, get_2d_array_2)
    print("sum of the matrices are {}".format(add_matrix))


if __name__ == '__main__':
    main()
