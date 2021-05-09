

def area(*vars):
    area_x = 1/2 * vars[0] * vars[1]
    return area_x


def main():
    b = int(input("Enter a value for b"))
    h = int(input("Enter value for h"))
    area_of_x = area(b, h)
    print("The are is {}".format(area_of_x))

if __name__ == '__main__':
    main()