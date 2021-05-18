"""
## Write a function to print range of prime numbers between two given numbers

Algorithm:

Step1: Get the two numbers from the user
Step2: Write a function - get n1 and n2 as arguments - function should return list of numbers
Step3: Initialise an empty list(prime_list=[]) to append the prime numbers to it.
Step3: write a loop to get values from n1 to n2
Step4: is_prime = True , Run a for loop from 2 to num -1
Step5: Check for the reminder is equal to Zero or not, if the remainder is equal to zero then its not a prime number, then set is_prime=False
Step6: If the remainder not equal to zero for all the numbers then append that number to the prime_list.
Step7: Return the prime_list.

"""

def prime(n1, n2):
    prime_list = []
    for i in range(n1, n2):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
               is_prime = False
               break
        if is_prime == True:
            prime_list.append(i)
    return prime_list


def main():
    n1 = int(input("Enter the first number: "))
#    n1 = 3
#    n2 = 15
    n2 = int(input("Enter the second number: "))
    get_prime = prime(n1,n2)
    print("The prime numbers are: ", get_prime)


if __name__ == "__main__":
    main()