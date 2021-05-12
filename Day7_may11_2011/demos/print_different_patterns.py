'''
11111
2222
333
44
5
'''

#for i in range(0,5):
#    for i in range(5):
#        print(i + 1 ,end="")
#    print("")

"""
k = 1
for i in range(5,0,-1):
    for j in range(i): # range(5) j 0,1,2,3,4 ... 55555...
        print(k, end="")
    k = k + 1
    print("")
"""


'''
1
33
555
7777
99999
'''

# k = 1
for i in range(1, 6): # 1 i=3 0,1
    for j in range(i):
        print((i * 2) - 1, end="")
#    k = k + 2
    print("")
