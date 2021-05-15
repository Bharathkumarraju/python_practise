"""
     *
    * *
   * * *
  * * * *
   * * *
    * *
     *

"""


num = int(input("Enter a Number to print astericks as daimond: "))
for i in range(num):
    print(" "*(num-i-1)+"* "*(i+1))
for i in range(num-1,0,-1):
    print(" "*(num-i)+"* "*(i))
