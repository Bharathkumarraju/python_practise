test = [1, 2, "hello", "test123", "hanuman", ["hello", "hi"]]


for i in test:
    print(i)


for i in enumerate(test):
    print(i)


for idx, item in enumerate(test):
    print(idx, type(item), item)



def test():
    print("SRI Anjaneyam")


if __name__ == '__main__':
    test()