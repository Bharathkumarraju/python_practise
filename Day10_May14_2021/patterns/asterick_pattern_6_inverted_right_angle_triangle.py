"""
* * * * *
* * * *
* * *
* *
*

"""

num = int(input("Enter number of rows"))
for i in range(num, 0 , -1):
    print("* "*i + " "*(num - i))

