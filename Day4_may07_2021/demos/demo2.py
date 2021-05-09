# input
# process
# output

def small_or_big(*vars):
    smaller = vars[0]
    greater = vars[1]
    if vars[0] < vars[1]:
        if vars[0] < vars[2]:
            smaller = vars[0]
        else:
            smaller = vars[2]
    elif vars[1] < vars[2]:
        smaller = vars[1]
    else:
        smaller = vars[2]

    if vars[0] > vars[1]:
        if vars[0] > vars [2]:
            greater = vars [0]
        else:
            greater = vars[2]
    elif vars[1] > vars[2]:
        greater = vars[1]
    else:
        greater = vars[2]

    return(smaller,greater)


def main():
    value_one = int(input("enter the the first value"))
    value_two= int(input("Enter the second value"))
    value_three = int(input("Enter the third value"))
    smaller, greater = small_or_big(value_one,value_two,value_three)
    print("the smaller numbers is {} and  the bigger number is {}".format(smaller, greater))

if __name__ == '__main__':
    main()




