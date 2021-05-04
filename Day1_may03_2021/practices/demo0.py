test = [1, 2, "hello", "test123", "hanuman", ["hello", "hi"]]
for i in test:
    print(i)

print("----------------------------------------")

for i in enumerate(test):
    print(i)

print("----------------------------------------")

for idx, item in enumerate(test):
    print(f"{idx}, {type(item)}, {item}")

print("----------------------------------------")

for idx, item in enumerate(test):
    print("{}, \t {},\t {}\t".format(idx, type(item), item))
