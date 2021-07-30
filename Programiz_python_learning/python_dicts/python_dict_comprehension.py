squares = { i: i*i for i in range(1,6)}
print(squares)

print("")

squares1 = {}
for i in range(1,12,3):
    squares1[i] = i*i
print(squares1)

print("")

# test = "hello!"
# for i in test:
#    print(test.count(i))



def charCount(s):
    d = {char:s.count(char) for char in s}
    print(d)
    for i in d.values():
        print(i)

charCount('Hello!')