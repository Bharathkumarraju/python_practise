"""
## Write a function to determine whether a given number is prime or not

Algorithm:

Step1: Get the number from the user(num)
Step2: Write a function - get num as an argument - function returns the num is prime or not
Step3: is_prime = True , Run a for loop from 2 to num -1
Step4: Check for the reminder is equal to Zero or not, if the remainder is equal to zero then its not a prime number, then set is_prime=False
Step5: If the remainder not equal to zero for all the numbers then its a prime number.

"""

def prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    return is_prime


def main():
    num = int(input("Enter a number: "))
    get_prime = prime(num)
    if get_prime == True:
        print("The number is prime")
    else:
        print("The number is not a prime")



if __name__ == "__main__":
    main()