"""
*
**
***
****
*****
"""

# range(1st, 2nd) --> In range 1st value is included and 2nd value is excluded.

n = int(input("enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")

