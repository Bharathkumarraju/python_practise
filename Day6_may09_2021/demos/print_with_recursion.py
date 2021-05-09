
def list_print(n):
    if len(n) == 0:
        return
    else:
        print(n[-1])
        n.pop()
        list_print(n)

def main():
    list_a = []
    for i in range(5):
        list_a.append(int(input("enter {} value".format(i + 1))))
    print_list = list_print(list_a)

if __name__ == '__main__':
    main()


