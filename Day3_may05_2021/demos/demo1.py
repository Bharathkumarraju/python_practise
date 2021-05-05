# input

# process

#output

def add(i, j):
    return(i + j)

def sub(i, j):
    return (i - j)

def mul(i, j):
    return (i * j)

def div(i, j):
    if j != 0:
        return (i/j)
    else:
        print("division by zero is not possible")

def main():
    a = int(input("Enter value for a"))
    b = int(input("Enter value for b"))
    sum_a = add(a, b)
    sub_a = sub(a, b)
    mul_a = mul(a, b)
    div_a = div(a, b)
    print("The addition of {}, {} is {}".format(a, b, sum_a))
    print("The subtraction of {}, {} is {}".format(a, b, sub_a))
    print("The multiplication of {} ,{} is {}".format(a, b, mul_a))
    print("The division of {}, {} is {}".format(a, b, div_a))


if __name__ == "__main__":
    main()