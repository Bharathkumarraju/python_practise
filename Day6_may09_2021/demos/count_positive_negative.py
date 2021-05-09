def find_pos_neg(n):
    pos = 0
    neg = 0
    for i in n:
        if i >= 0:
            pos = pos + 1
        else:
            neg = neg + 1
    return(pos, neg)

def main():
    list_a = []
    for i in range(7):
        list_a.append(int(input("enter {} element: ".format(i + 1))))
    pos, neg = find_pos_neg(list_a)
    print("The count of positive elements are {} and the count of negative elements are {}  ".format(pos, neg))

if __name__ == '__main__':
    main()
