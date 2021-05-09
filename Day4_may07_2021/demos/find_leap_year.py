def leap(n):
    if n % 4 == 0:
        return True
    else:
        return False

def main():
    year = int(input("enter the year"))
    leap_year = leap(year)
    print("The entered year is leap {}".format(leap_year))


if __name__ == '__main__':
    main()