
def check_num(num):
    if num > 0:
        return("Positive")
    elif num < 0:
        return("Negative")
    else:
        return("Zero")


def main():
    num = int(input("Enter a number!!!"))
    value=check_num(num)
    print("The entered value is {}".format(value))



if __name__ == '__main__':
    main()