'''
x: 5
y: 1

x = 6  # x + y
y = x - y # 6 - 1 ( x = 6  and y = 5)
x = x - y # 6 - 5
'''

def swap(*vars):
     x = vars[0]
     y = vars[1]
     x = x + y
     y = x - y
     x = x - y
#    temp = x
#    x = y
#    y = temp
#    x, y = y, x
     return(x, y)

def  main():
    x = int(input("Enter the value for x"))
    y = int(input("Enter the value for y"))
    x, y = swap(x, y)
    print("the values swapped are {} , {}".format(x, y))

if __name__ == '__main__':
    main()