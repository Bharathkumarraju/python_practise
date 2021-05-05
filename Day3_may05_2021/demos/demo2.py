
#input + - 0

#process

#output

def calculate(i):
    if i < 0:
        return("negative")
    elif i > 0:
        return("positive")
    else:
        return("zero")

def main():
    a = int(input("Enter a number"))
    value =  calculate(a)
    print("The number is {}".format(value))


if __name__ == "__main__":
    main()