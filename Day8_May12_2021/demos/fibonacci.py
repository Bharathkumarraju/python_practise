"""
1 1 2 3 5 8 13 21 34...
a b s
  a b s
    a b s
"""
a = 1
b = 1
print(a)
print(b)
for i in range(8):
    s = a + b
    a = b
    b = s
    print(s)
