# Input list_a = [1, 2, 3, [4, 5, 6], 7, [8, 9], 10]
#def getsum(n):
#    sum = 0
#    for i in n:
#        if isinstance(i, int):
#            sum = sum + i
#        else:
#            for j in i:
#                sum = sum + j
#    return sum
def getsum(n):
    sum = 0
    for i in n:
        if isinstance(i, int):
            sum = sum + i
        else:
            sum = sum + getsum(i)
    return sum

def main():
    list_a = [1, 2, 3, [4, 5, 6], 7, [8, 9], 10]
    the_sum = getsum(list_a)
    print("The sum of elements in a nested list is: {} ".format(the_sum))

if __name__ == '__main__':
    main()