"""
1. open a file
r - read mode
w - write mode
a - append mode
2. Perform operations
3. close a file


"""

try:
    f = open("messages.txt", 'r')
    content_6_chars = f.read(6)
    print(content_6_chars)

    more_content =  f.read(12)
    print(more_content)
finally:
    f.close()