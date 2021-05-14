"""
*******
 *****
  ***
   *
"""
# for i in range(1,11,2):
#     print(i)
#
# print("-----------------------------")
#
# for i in range(5, 0, -1):
#     print(i)
#
# print("-----------------------------")

num = int(input("Enter a value"))
for i in range(num, 0, -1):
    for j in range(0, num-i):
        print(" ", end="")
    for j in range(0, i):
        print("* ", end="")
    print()