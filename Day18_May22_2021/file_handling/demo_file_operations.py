"""
1. open a file
r - read mode
w - write mode
a - append mode
2. Perform operations
3. close a file


"""

f = open("messages.txt", 'r')

for i in f:
    print(i)