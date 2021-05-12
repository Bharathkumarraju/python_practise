def print_recurse(n):
    i = 0
    if i < len(n):
        print(n[i])
        print_recurse(n[1:])

def main():
    list_a = [1, 2, 3, 4, 5, 7, 8, 9]
    print_recurse(list_a)
#    get_list = print_recurse(list_a)
#    print("The list print with recursion is {} ".format(get_list))


if __name__ == '__main__':
    main()

# Stopping condition
# Recursing condition