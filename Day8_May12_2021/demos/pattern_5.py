'''
    1
   12
  123
 1234
12345
'''


def triangle(n):
    k = n - 1
    for i in range(1, n + 1):
        for x in range(k):
            print(" ", end="")
        k = k - 1
        for j in range(1, i + 1):
            print(j, end="")
        print("")

triangle(5)