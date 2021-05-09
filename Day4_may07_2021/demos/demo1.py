# 1/2bh

def area(**vars):
    area_of_x = 1/2 * vars["breadth"] * vars["height"]
    return area_of_x

def  main():
    b = int(input("Enter the value for b"))
    h = int(input("Enter the value for h"))
    area_a = area(breadth=b, height=h)
    print("The area of x is {}".format(area_a))

if __name__ == '__main__':
    main()





