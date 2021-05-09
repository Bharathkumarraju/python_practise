
def find_a_value(*args):
    list_b = args[0]
#    if args[1]:
#        c = args[1]
#    else:
#        c = int(input("Enter a value"))
    if len(args) == 2:
        c = args[1]
    else:
        c = int(input("Enter a value"))
    if c in list_b:
        return True
    else:
        return False

def main():
    list_a = []
    for i in range(5):
        list_a.append(int(input("Enter {} value".format(i + 1))))
    get_value = int(input("Enter a value to findout whether this is inside the list or not"))
    found_value = find_a_value(list_a, get_value)
    if found_value == True:
        print("The value entered {} is in the list".format(get_value))
    else:
        print("The value entered {} is not in the list".format(get_value))

    found_value2 = find_a_value(list_a)
    if found_value2 == True:
        print("The value entered is in the list")
    else:
        print("The value entered is not in the list")

if __name__ == '__main__':
    main()