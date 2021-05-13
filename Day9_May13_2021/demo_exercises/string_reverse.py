n = input("Enter a word: ")
print("the entered string is: ", n)

reversed_string = ""
for i in n:
    reversed_string = i + reversed_string
print("The reverse string is: ", reversed_string)
