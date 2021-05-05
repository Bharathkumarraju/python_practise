""" Topics 

List 
Set, Tuples, Dictionary
Nesting 
Functions 

Live Exercises 
""" 
# import time

# a = [1,2,3,4,5,6,7,8,9,10]
# # a_new = [False, True,...]
# # Create a new list, where it check if the number is even/odd, and stores that value
# a_new = []
# ### List comprehension 

# def is_even(val): 
# 	if val % 2 ==0: 
# 		return True
# 	else: 
# 		return False 

# t1 = time.time()

# a_new = [x * 2 for x in a]
# print(a_new)
# a_new = [is_even(x) for x in a]
# diff = time.time()-t1 
# print(diff)
# b_new = []
# t2 = time.time()
# for x in a: 
# 	a_new.append(is_even(x))
# diff_2 = time.time() - t2
# print(diff, diff_2)

## set, tuples,dictionary 
"""
"""
# list_a = [1,2,2,1,1,2] 
# list_a[1] = 10
# Set =set(1,2,3,12)
# set_a[1] = 14
# set_a.append(12)

# List, Tuple, Dictionary, Set

# def integer_va(): 

# 	return (1,2,3)

# a,b,c = integer_va()

# 3.

# diction = {
# 	"name": "sakar", "name": "ghimire"
# }

# print(diction)




# Nesting - One data type within the scope another 

# list_a = [[1,2,3],]

# diction = 	

#Code Reusability 

# a + b + c
# a + b + c
# a+b+c

# def add(a,b,c): 
# 	return (a+b+c, a*b*c)

# sum=add(a,b,c)



### Print the factorial of a number 

'''
Input - Number (ask number from user using input function )

Processing - n * n-1 * n-2 .... * 1

Output - Factorial of the number 

'''
# 1,2,3,4,5,6,7,...n


# range (intial value, final value, step value)


def print_even(): 
	for x in range(0,100,2): 
		print(x)


def fact(n):
	factorial = 1 
	for x in range(n,1,-1): 
		factorial = factorial * x
	return(factorial)

	 


def main(): 
	# n = int(input("Enter a number"))

	# factorial = fact(n)
	# print("The factorial of {} is {}".format(n, factorial))
	print_even()

if __name__ == "__main__": 
	main()