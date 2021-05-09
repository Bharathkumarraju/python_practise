"""
Course Plan May 7
Arbitary Arguments 
Keyword Arguments 

While Loop 
For Loop

Programming Assignments 

""" 

## Arguments
# def my_function(**var): 
# 	# print(name[0],name[2],name[3])
# 	print(var["name"],var["last_name"])

# # name ["sakar","Ghimire",25]

# my_function(name = "Sakar",last_name = "Ghimire",age = 25,temp = "Hello")
# my_function("Sakar","Ghimire")



"""Python Loops 
3 types -: 
For Loop 
While Loop 
Do While Loop 

for x in range(10,10,1): 
	
	break 
	continue



"""
# while True: 


# for i in range(10):
# 	if i == 5: 
# 		break 
# 	print(i)
# else: 
# 	print("exitting the program")


## Recursion

### factorial 
# n , n - 1, n-2, n-3,....1
n = 5 

# 120
# return(5 * 24)
# return(5* 4*6)
# return(5*4*3*2)
# return(5*4*3*2*1)
# return(5*4*3*2*1)



def fact(n):
	# factorial = 1 
	# print("inside fact")
	if n == 1: 
		return 1
	else: 
		return(n * fact(n-1))

def main(): 
	n = int(input("Enter value of n"))
	factorial_of_n = fact(n)
	print("The factorial of n is",factorial_of_n)


if __name__ == "__main__": 
	main()






####
# Write a program to swap values of two variables 
# 		for example : if a = 1 and b = 2, the value should be swapped to a =2 and b = 1

### Write a program to check if a given year is leap year or not 
# 		For example : if year = 2020, program should say "leap year"
#					and if year = 2021, program should say "Not a leap year"


