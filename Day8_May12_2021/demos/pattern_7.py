"""
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""

def multiples_three_five():
    for i in range(1, 51):
        if(i%5 == 0 and i%3 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    multiples_three_five()


if __name__ == '__main__':
    main()


