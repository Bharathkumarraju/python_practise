'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

k = 1
for i in range(1, 10):
    for j in range(k):
        print("*", end="")
    if i < 5:
        k = k + 1
    else:
        k = k - 1
    print("")
